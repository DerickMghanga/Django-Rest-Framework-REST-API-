import json
from django.http import JsonResponse


def api_home(request, *args, **kwargs):
    request.body
    body = request.body # byte string of JSON data

    data = {}
    try:
        data = json.loads(body)  # parses a JSON string and returns a dict(python object)
    except:
        pass

    print(data)
    return JsonResponse(data)