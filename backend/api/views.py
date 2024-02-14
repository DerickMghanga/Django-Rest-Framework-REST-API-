import json
from django.http import JsonResponse, HttpResponse
from django.forms.models import model_to_dict  #converts models to dict

from products.models import Product

def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()  #gets a random query and selects the first item
    data = {}

    if model_data:  #if the model exists.(sometimes it may not exist)
        data = model_to_dict(model_data, fields=["id", "title", "price"])
    return JsonResponse(data)
    #     json_data_str = json.dumps(data)
    # return HttpResponse(json_data_str, headers={"content-type": "application/json"})

    #JsonResponse accepts 'dict' data types only
    #HttpResponse accepts 'str' data types only