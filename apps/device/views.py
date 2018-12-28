from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import requests
import json
from datetime import datetime

from .models import Stoken

# Create your views here.


def gettoken(request):
    if request.method == "GET":
        return render(request, 'index.html')
    else:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if Stoken.objects.filter(expires_in__gt=now).count() > 0:
            access_token = Stoken.objects.order_by('-expires_in')[0].access_token
        else:
            expires_in = request.POST.get('expires_in')
            access_token = request.POST.get('access_token')
            #req = requests.post("https://api.parkline.cc/api/token", data={"apiid":apiid, "apikey":apikey}, headers={'user-agent': 'my-app/0.0.1'})
            Stoken.objects.create(expires_in=expires_in, access_token=access_token)

        print(Stoken.objects.all().count())

        return HttpResponse("OK!")
