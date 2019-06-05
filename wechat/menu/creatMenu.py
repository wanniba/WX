import urllib
from urllib import parse
from urllib.parse import urlencode

import requests
import json

address = 'http://3w4gvh.natappfree.cc/index'
appid = 'wx5cdbf5d00cff05bc'
secret = '727d7976a695314d7e223acdfce8cdde'

tokenUrl = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=" + appid + "&secret=" + secret
headers = {"Content-type": "application/json"}
tokenResp = requests.get(tokenUrl, headers=headers)
access_token = tokenResp.json()['access_token']
print("获取token成功" + tokenResp.json()['access_token'])
redirect_uri = address
# 需要对url编码处理  处理编码中的/
redirect_uri=urllib.parse.quote(redirect_uri, safe='')
# redirect_uri = urlencode(c)
gotoUrl = "https://open.weixin.qq.com/connect/oauth2/authorize?appid=" + appid + "&redirect_uri=" + redirect_uri + "&response_type=code&scope=snsapi_base&state=123#wechat_redirect"
print (gotoUrl)
menu = {
    "button": [
        {
            "type": "click",
            "name": "今日歌曲",
            "key": "V1001_TODAY_MUSIC"
        },
        {
            "name": "菜单",
            "sub_button": [
                {
                    "type": "view",
                    "name": "跳转",
                    "url": gotoUrl
                },

                {
                    "type": "click",
                    "name": "赞一下我们",
                    "key": "V1001_GOOD"
                }]
        }]
}
print(type(menu))
menuJson = json.dumps(menu, ensure_ascii=False).encode('utf-8')
print(menuJson)

# 设置menu
setMenuUrl = 'https://api.weixin.qq.com/cgi-bin/menu/create?access_token=' + access_token
setMenuResp = requests.post(setMenuUrl, menuJson)
access_token = tokenResp.json()['access_token']
print("设置菜单" + str(setMenuResp.json()['errcode']) + setMenuResp.json()['errmsg'])
