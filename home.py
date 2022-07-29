from mainMenu import showMenu
from apiFunctions.marketHours import get_marketHours
from apiFunctions.movers import get_Movers

userPull=showMenu()

if(userPull==1):
    print(get_marketHours())

if(userPull==2):
    print(get_Movers())