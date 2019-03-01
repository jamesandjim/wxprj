from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, HttpResponseServerError
import requests
import json
from datetime import datetime
from django.utils import timezone
from django.views.generic import View

from device.WechatApi import WechatLogin
from .models import Stoken

# Create your views here.

#获取微信一般访问的令牌
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



#以下为取得微信用户信息功能
class WechatViewSet(View):
    wechat_api = WechatLogin()


class AuthView(WechatViewSet):
    def get(self, request):
        url = self.wechat_api.get_code_url()
        return redirect(url)


class GetInfoView(WechatViewSet):
    def get(self,request):
        if 'code' in request.GET:
            code = request.GET['code']
            token, openid = self.wechat_api.get_access_token(code)
            if token is None or openid is None:
                return HttpResponseServerError('get code error')
            user_info, error = self.wechat_api.get_user_info(token, openid)
            if error:
                return HttpResponseServerError('get access_token error')
            user_data = {
                'nickname': user_info['nickname'],
                'sex': user_info['sex'],
                'province': user_info['province'].encode('iso8859-1').decode('utf-8'),
                'city': user_info['city'].encode('iso8859-1').decode('utf-8'),
                'country': user_info['country'].encode('iso8859-1').decode('utf-8'),
                'avatar': user_info['headimgurl'],
                'openid': user_info['openid']

            }
           


