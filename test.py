from urllib import response
import requests
from authData import apikey
from authData import quotesURL

parameters={"apikey":apikey,"symbol":"AAPL"}

response=requests.get(quotesURL,params=parameters)

data=response.json()

print(data['AAPL']["assetType"])