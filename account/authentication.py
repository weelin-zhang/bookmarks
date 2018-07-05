from django.contrib.auth.models import User
from django.conf import settings
import ldap

class EmailAuthBackend(object):
    """
    Authenticate using e-mail account.
    """
    def authenticate(self, username=None, password=None):
        print(self.__class__.__name__)
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


class LDAPAuthBackend(object):
    """
    Authenticate using e-mail account.
    其它方式验证不通过时使用
    """
    def authenticate(self, username=None, password=None):
        print(self.__class__.__name__)
        try:
            conn = ldap.initialize(settings.LDAP_AUTH_URL)
            # 是否存在用户
            r = conn.search_s(settings.LDAP_AUTH_SEARCH_BASE, ldap.SCOPE_SUBTREE, "mail={}".format(username))
            if not r:
                return None
            # 存在用户获取dn
            dn = f"{r[0][0]}"
            # 认证
            exists = conn.simple_bind_s(dn, password)
            print(exists)
            # 存一下
            new_user = User()
            new_user.username = new_user.email = username
            new_user.set_password(password)
            new_user.save()
            user = User.objects.get(username=username, email=username)
            return user
        except ldap.INVALID_CREDENTIALS:
            print("ldap.INVALID_CREDENTIALS")
            return None
        except Exception as e:
            print(e)
            return None
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
