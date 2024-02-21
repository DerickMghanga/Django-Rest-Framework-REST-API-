#import json
#from django.http import JsonResponse, HttpResponse
from django.forms.models import model_to_dict  #converts models to dict
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer

@api_view(["POST"])
def api_home(request, *args, **kwargs):
    """
    Django Rest Framework API VIEW
    """
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True): #checks if the data is aligned with the serializer(models)
        #instance = serializer.save() #similar to forms.save()
        print(serializer.data)
        return Response(serializer.data)
    return Response({"invalid":"Not good data"}, status=400)
    


    
    #'GET' REQUEST CODE
    # instance = Product.objects.all().order_by("?").first()  #gets a random query and selects the first item
    # data = {}

    # if instance:  #if the model exists.(sometimes it may not exist)
    #     #data = model_to_dict(instance, fields=["id", "title", "price", "sale_price"])
    #     data = ProductSerializer(instance).data
   




    #     json_data_str = json.dumps(data)
    # return HttpResponse(json_data_str, headers={"content-type": "application/json"})

    #JsonResponse accepts 'dict' data types only
    #HttpResponse accepts 'str' data types only