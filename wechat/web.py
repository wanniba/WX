import hashlib

import requests
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from wechat.replay.autoreply import autoreply
import json

@csrf_exempt
def index(request):
    # address = 'http://3w4gvh.natappfree.cc/index'
    # appid = 'wx5cdbf5d00cff05bc'
    # secret = '727d7976a695314d7e223acdfce8cdde'
    #
    # print('into index')
    # code = request.GET.get('code', str)
    # state = request.GET.get('state', str)
    #
    # web_token_url = "https://api.weixin.qq.com/sns/oauth2/access_token?appid="+appid+"&secret="+secret+"&code="+code+"&grant_type=authorization_code"
    #
    # responce =requests.get(web_token_url)
    # print(responce.text)
    # resp = json.loads(responce.text)
    #
    # access_token = resp['access_token']
    # expires_in= resp['expires_in']
    # refresh_token= resp['refresh_token']
    # openid= resp['openid']
    # print(access_token)
    # # ======================获取用户信息========================
    # get_user_url = "https: // api.weixin.qq.com / sns / userinfo?access_token = "+access_token+" & openid = "+openid+" & lang = zh_CN"
    # user_responce = requests.get(get_user_url)
    # print(user_responce.text)
    # user_resp = json.loads(user_responce.text)
    
    context = {}
    # context['hello'] =str(refresh_token+"==="+openid)
    return render(request, 'hello.html', context)
