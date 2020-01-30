from Robinhood import Robinhood
from myFunc import get_Prices

my_trader = Robinhood()
try_signin = True
while(try_signin):
    try:
        my_trader.login(username="", password="")
        try_signin = False
        signin = True

    except:
        retry = input("Error Logging in! \n Would you like to try Again (y) (n)")
        if(retry == 'n'):
            try_signin = False
            signin = False

if(signin):
    get_Prices('APPL')
