# Mock function
def connectToBank(user):
    return "1234"

def validatePIN(pin, user):
    bank_pin = connectToBank(user)

    if bank_pin == pin:
        return True
    else:
        return False

def userAuthentication(user):
    pin = input("Enter PIN#: ")

    if len(pin) == 4:
        if validatePIN(pin, user):
            return True
        else:
            return False
    else:
        return False


