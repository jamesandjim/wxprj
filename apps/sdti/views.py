from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.utils.encoding import smart_str
from django.conf import settings

from lxml import etree
import hashlib
import time
import os


def CheckSign(requests):
    os.getpid()
    form = {}
    form['signature'] = requests.GET.get('signature', None)
    form['timestamp'] = requests.GET.get('timestamp', None)
    form['nonce'] = requests.GET.get('nonce', None)
    form['token'] = settings.TOKEN
    Signature = form.pop('signature')
    Key = hashlib.sha1("".join(sorted([form[i] for i in form])).encode('utf-8')).hexdigest()  # 获得sha1加密后结果
    return True if Signature == Key else False


@csrf_exempt
def wx(requests):  # URL路由入口
    if requests.method == "GET":
        EchoStr = requests.GET.get('echostr', None)  # 获取回应字符串
        return HttpResponse(EchoStr) if CheckSign(requests) else HttpResponse('vaild signature')
    elif requests.method == "POST":
        if CheckSign(requests) == False:
            print('check not pass')
            return None
        Res = smart_str(requests.body)
        xml = etree.fromstring(Res)
        fromUser = xml.find('ToUserName').text
        toUser = xml.find('FromUserName').text
        msgType = xml.find('MsgType').text
        nowtime = str(int(time.time()))

        if msgType == 'text': content = xml.find('Content').text
        rendered = {'toUser': toUser, 'fromUser': fromUser, 'nowtime': nowtime,
                                                        'content': '文本消息，功能正在开发中'}
        return render(requests,'index.html',rendered)

    else:
        return HttpResponse('invaild requests')


