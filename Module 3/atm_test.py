import atm_authentication

user = []

if atm_authentication.userAuthentication(user):
    print("Authentication Validated")
else:
    print("Authentication Error")