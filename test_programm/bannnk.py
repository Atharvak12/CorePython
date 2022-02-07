
from req import InsufficientBalance
balance = 1000
def withdreaw(amount=0):
    if(amount>=balance or amount<0 ):
        raise InsufficientBalance()
    else:
        print("Net ammount", balance-amount)

try :
    withdreaw(5000)
except InsufficientBalance as e:
    print(e)