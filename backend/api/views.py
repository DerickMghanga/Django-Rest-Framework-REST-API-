import json
from django.http import JsonResponse


def api_home(request, *args, **kwargs):
    #request.body
    print(request.GET)
    body = request.body # byte string of JSON data
    data = {}
    try:
        data = json.loads(body)  # parse a JSON string and returns a dict(python object)
    except:
        pass
    print(data)
    data['headers'] = dict(request.headers)
    #print(dict(request.headers))
    #json.dumps(dict(request.headers)) # change the headers(dict) to json string
    data['content_type'] = request.content_type
    data['params'] = dict(request.GET)
    

    return JsonResponse(data)