from mainMenu import showMenu
from apiFunctions.marketHours import get_marketHours
from apiFunctions.movers import get_Movers
from apiFunctions.liveQuotes import get_quotesData
from apiFunctions.priceHistory import get_priceHistory

userPull=showMenu()

if(userPull==1):
    print(get_marketHours())

if(userPull==2):
    print(get_Movers())

if(userPull==3):
    print(get_priceHistory())

if(userPull==4):
    print(get_quotesData())
