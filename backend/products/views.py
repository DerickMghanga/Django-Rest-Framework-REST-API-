from rest_framework import generics, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.http import Http404
from django.shortcuts import get_object_or_404

from .models import Product
from .serializers import ProductSerializer


#Create and list view
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        #serializer.save(user=self.request.user)
        #print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)
product_list_create_view = ProductListCreateAPIView.as_view()

#Get specific details
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk' (primary key)
product_detail_view = ProductDetailAPIView.as_view()

#Update specific details
class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk' #(primary key)

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
product_update_view = ProductUpdateAPIView.as_view()

#Delete specific details
class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk' #(primary key)

    def perform_destroy(self, instance):
        #instance
        super().perform_destroy(instance)
product_destroy_view = ProductDestroyAPIView.as_view()


# class ProductListAPIView(generics.ListCreateAPIView):
#     '''
#     Not gonna use this method
#     '''
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     # lookup_field = 'pk' (primary key)
# product_list_view = ProductListAPIView.as_view()


#Class based Views using Mixins("CREATE", "LIST" and "GET")
class ProductMixinView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
    ):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'  # used by the RetrieveModelMixin
    
    def get(self, request, *args, **kwargs):  #HTTP --> GET (all and specific details)
        #print (args, kwargs)
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs): #HTTP --> POST
        return self.create(request, *args, **kwargs)
    
    #def put
    #def delete
product_mixin_view = ProductMixinView.as_view()



#Function Based Views for Create and List for Products
@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method

    if method == 'GET':
        if pk is not None:
            #get request -> detail view
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)
        
        #else >> list view.  (return all Products)
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)

    if method == 'POST':
        #create an item
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True): #checks if the data is aligned with the serializer(models)
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        
        return Response({"invalid":"Not good data"}, status=400)