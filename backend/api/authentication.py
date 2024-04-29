from  rest_framework.authentication import TokenAuthentication as BaseTokenAuth


class TokenAuthentication(BaseTokenAuth):  # Over-ride the deafult token name >> custom token name
    keyword = 'Bearer'  # changes from default 'Token' to 'Bearer'