from operator import index
import requests
from accessData.authData import apikey
from accessData.url import moversURL

def set_IndexUrl():
    print(" ")
    print("Which index do you want top movers for?")
    print("---------------------------------------")
    print("1) Nasdaq")
    print("2) Dow Jones")
    print("3) S&P 500")
    print("----------------------------------------")
    userIndex=int(input("Enter the corresponding number(one argument only): "))
    print("-----------------------------------------------------------------")
    if(userIndex==1):
        updateURL=moversURL.format(index="$COMPX")
    if(userIndex==2):
        updateURL=moversURL.format(index="$DJI")
    if(userIndex==3):
        updateURL=moversURL.format(index="$SPX.X")

    return updateURL

def set_direction():
    userDirection=str(input("Enter UP for largest positive movers or DOWN for largest negative movers: ")).lower()
    print("--------------------------------------------------------------------------------------------")
    return userDirection

def set_ChangeType():
    userChangeType=str(input("Enter the specific change format(VALUE or PERCENT): ")).lower()
    print("-----------------------------------------------------------------------")
    return userChangeType

def set_Parameters():
    parameters={"apikey":apikey,"direction":set_direction(),"change":set_ChangeType()}
    return parameters

def get_Movers():
    response=requests.get(set_IndexUrl(),params=set_Parameters())
    return response.json()
