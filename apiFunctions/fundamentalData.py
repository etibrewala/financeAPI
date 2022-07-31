from symtable import Symbol
import requests
from accessData.authData import apikey
from accessData.url import fundDataURL

def get_Symbol():
    userSymbol=str(input("Which company do you want fundamental data for(enter stock symbol)? ")).upper()
    print("-----------------------------------------------------------------------------------")

    return userSymbol

def get_FundamentalData():
    stockSymbol=get_Symbol()
    symbolSearchParams={"apikey":apikey,
                        "symbol":stockSymbol,
                        "projection":"symbol-search"}
    
    fundDataParams={"apikey":apikey,
                    "symbol":stockSymbol,
                    "projection":"fundamental"}

    symbolSearchData=requests.get(fundDataURL,params=symbolSearchParams)
    fundamentalData=requests.get(fundDataURL,params=fundDataParams)
    
    userData=int(input("Enter 1 for SYMBOL DATA or 2 for FUNDAMENTAL DATA: "))
    print("-----------------------------------------------------------------")

    if(userData==1): return symbolSearchData.json()

    if(userData==2): return fundamentalData.json()

