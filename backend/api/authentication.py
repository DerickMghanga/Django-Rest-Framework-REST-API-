from  rest_framework.authentication import TokenAuthentication as BaseTokenAuth


class TokenAuthentication(BaseTokenAuth):  # Over-ride the deafult token name
    keyword = 'Bearer'