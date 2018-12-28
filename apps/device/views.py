from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import requests
import json

# Create your views here.

def gettoken(request):
    if request.method == "GET":
        return render(request, 'index.html')
    # else:
    #     apiid = request.POST.get('apiid')
    #     apikey = request.POST.get('apikey')
    #     req = requests.post("https://api.parkline.cc/api/token", data={"apiid":apiid, "apikey":apikey}, headers={'user-agent': 'my-app/0.0.1'})
    #
    #     return JsonResponse(req.text, safe=False)
