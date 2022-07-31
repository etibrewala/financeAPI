import requests
from accessData.authData import apikey
from accessData.url import marketsURL

def set_marketParams():
    print(" ")
    print("Which markets would you like hours for?")
    print("---------------------------------------")
    print("1) EQUITY")
    print("2) OPTION")
    print("3) FUTURE")
    print("4) BOND")
    print("5) FOREX")
    print("---------------------------------------")
    userMarkets=str(input("Enter markets NAME(seperate with comma if more than one): ")).upper()
    print("--------------------------------------------------------------------------")
    parameters={"apikey":apikey, "markets":userMarkets}
    return parameters

def get_marketHours():
    response=requests.get(marketsURL,params=set_marketParams())
    return response.json()
