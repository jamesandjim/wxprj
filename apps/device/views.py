from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import requests
import json
from datetime import datetime
from django.utils import timezone

from .models import Stoken

# Create your views here.


def gettoken(request):
    if request.method == "GET":
        access_token = '0'
        now = timezone.now()
        b = Stoken.objects.all().order_by('-expires_in')[0]

        if b is not None:
            expires_in = b.expires_in

            if expires_in.strftime( '%Y-%m-%d %H:%M:%S %f') > now.strftime('%Y-%m-%d %H:%M:%S %f'):
                access_token = b.access_token

        return render(request, 'index.html', {"access_token":access_token})
    else:
        now = timezone.now()
        b = Stoken.objects.all().order_by('-expires_in')[0]
        if b is not None:
            access_token = b.access_token
        else:
            expires_in = request.POST.get('expires_in')
            access_token = request.POST.get('access_token')
            #req = requests.post("https://api.parkline.cc/api/token", data={"apiid":apiid, "apikey":apikey}, headers={'user-agent': 'my-app/0.0.1'})
            Stoken.objects.create(expires_in=expires_in, access_token=access_token)

        print(Stoken.objects.all().count())

        return HttpResponse("OK!")
