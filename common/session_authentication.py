from rest_framework.authentication import SessionAuthentication

# csrf check not required for REST API
class CsrfExecptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening