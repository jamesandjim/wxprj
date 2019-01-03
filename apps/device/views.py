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
        expires_in = '0'
        now = timezone.now()
        b = Stoken.objects.filter(tid='99')[0]

        if b is not None:
            expires_in = b.expires_in

            if expires_in > now.strftime('%Y-%m-%d %H:%M:%S %f'):
                access_token = b.access_token
                expires_in = b.expires_in

        return render(request, 'index.html', {"expires_in": expires_in, "access_token": access_token})
    else:
        status = 'old'
        ntype = request.POST.get('ntype')
        expires_in = request.POST.get('expires_in')
        access_token = request.POST.get('access_token')
        if ntype == 'new':
            Stoken.objects.filter(tid='99').update(expires_in=expires_in, access_token=access_token)
            status = 'new'
            return render(request, 'index.html', {"expires_in": expires_in, "access_token": access_token})




