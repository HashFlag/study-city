import json
from django.contrib.auth.backends import ModelBackend, UserModel
from django.db.models import Q
from django.conf import settings
from urllib.parse import urlencode
from urllib.request import urlopen
from luffyapi.settings import constants


class AuthModelBackend(ModelBackend):
    """ 自定义认证类 """
    def authenticate(self, request, username=None, password=None, **kwargs):
        # 校验验证码票据是否正确
        if kwargs.get("ticket") and request is not None:
            result = self.check_ticvket(kwargs.get("ticket"), kwargs.get("randstr"), request._request.META["REMOTE_ADDR"])
            if not result:
                return None
        try:
            user = UserModel.objects.get(Q(username=username) | Q(mobile=username))
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
        except UserModel.DoesNotExist:
            return None

    def check_ticvket(self, ticket, randstr, user_id):
        """
        验证防水墙验证码返回的临时票据方法
        :param ticket: 临时票据[客户端上传过来的]
        :param randstr: 随机数[腾讯服务器主动添加的,要求我们验证的时候必须原样返回]
        :param user_ip: 客户端的IP
        :return: boolean
        """
        params = {
            "aid": settings.TENCENT_CAPTCHA["APPID"],
            "AppSecretKey": settings.TENCENT_CAPTCHA["App_Secret_Key"],
            "Ticket": ticket,
            "Randstr": randstr,
            "UserIP": user_id
        }
        params = urlencode(params).encode()
        url = settings.TENCENT_CAPTCHA["GATEWAY"]
        f = urlopen(url, params)
        content = f.read()
        res = json.loads(content)
        if res:
            error_code = res["response"]
            if error_code == "1":
                return True
        return False


def jwt_response_payload_handler(token, user=None, request=None):
    """
    jwt自定义响应数据
    :param token: jwt token
    :param user: 用户模型对象
    :param request: 本次客户端的请求对象
    :return: 字典, 返回值
    """
    return {
        'token': token,
        'user_id': user.id,
        'avatar': user.avatar.url if user.avatar else "",
        'nickname': user.name if user.name else "",
        # 返回用户积分和换算比例
        'user_credit': user.credit,
        'credit_rmb': constants.RMB_CREDIT,
    }



