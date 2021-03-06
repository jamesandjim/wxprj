"""
微信公众号的配置信息
"""

#公众号APPID
APPID = ''
#公众号APPSECRET
APPSECRET = ''


#商户ID
MCH_ID = ''
API_KEY = ''


# ----------------------------------------------回调页面---------------------------------------------- #
# 用户授权获取code后的回调页面，如果需要实现验证登录就必须填写

REDERECT_URI = ''
PC_LOGIN_REDIRECT_URI = ''

defaults = {
    # 微信内置浏览器获取code微信接口
    'wechat_browser_code': 'https://open.weixin.qq.com/connect/oauth2/authorize',
    # 微信内置浏览器获取access_token微信接口
    'wechat_browser_access_token': 'https://api.weixin.qq.com/sns/oauth2/access_token',
    # 微信内置浏览器获取用户信息微信接口
    'wechat_browser_user_info': 'https://api.weixin.qq.com/sns/userinfo',
    # pc获取登录二维码接口
    'pc_QR_code': 'https://open.weixin.qq.com/connect/qrconnect',
    # pc获取登录二维码接口
    #'pc_QR_code': 'https://api.weixin.qq.com/sns/userinfo',

}


SCOPE = 'snsapi_userinfo'
PC_LOGIN_SCOPE = 'snsapi_login'
STATE = ''
LANG = 'zh_CN'