import requests
from accessData.authData import apikey
from accessData.url import quotesURL

def set_quoteParams():
    userSymbols=str(input("Enter the stock SYMBOLS for which you want quotes(seperate with comma if more than one): ")).upper()
    print("---------------------------------------------------------------------------------------------------------")
    parameters={"apikey":apikey,"symbol":userSymbols}
    return parameters

def get_quotesData():
    reponse=requests.get(quotesURL,params=set_quoteParams())
    return reponse.json()