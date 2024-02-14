import json
from django.http import JsonResponse

from products.models import Product

def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()  #gets a random query and selects the first item
    data = {}

    if model_data:  #if the model exists.(sometimes it may not exist)
        data["id"] = model_data.id   # id field comes by default in models creation
        data["title"] = model_data.title
        data["content"] = model_data.content
        data["price"] = model_data.price

    return JsonResponse(data)