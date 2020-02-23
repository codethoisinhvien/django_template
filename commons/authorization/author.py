from rest_framework.permissions import BasePermission
from rest_framework import HTTP_HEADER_ENCODING
import casbin
from .adapter import Adapter
class IsAuthor(BasePermission):
    def __init__(self):
        self.enforcer = casbin.Enforcer("model.conf", Adapter)
    def has_permission(self):
        self.enforcer.add_policy(ptype='p', v0='alice', v1='data1', v2='read')
        # hearder = self.get_header(request)
        #
        # if hearder is None:
        #     return False
        #
        # try:
        #     role=1
        #
        #     return False
        #
        # except Exception as e:
        #     print(e)
        #     return False

    def get_header(self, request):
        """
            user = api_settings.JWT_PAYLOAD_HANDLER(hearder)
            print(user['role'] == 2)
            if (user['role'] == 2):
                return True
        Extracts the header containing the JSON web token from the given
        request.
        """
        header = request.META.get('HTTP_AUTHORIZATION')

        if isinstance(header, str):
            # Work around django test client oddness
            header = header[7:len(header)]
            header = header.encode(HTTP_HEADER_ENCODING)

        return header
