import requests
import colorama
from colorama import Fore

## single ip request
#requests.get function returns a json object of the result.
#we used ip-api.com to retrieve the current public ipv4 and ipv6 address.com
response = requests.get("http://ip-api.com/json/110.50.224.0?fields=query,status,country,countryCode,region,regionName,city,lat,lon,timezone,isp,org,as,continent,hosting").json()
print(Fore.WHITE + "=============================================")
print(Fore.YELLOW +"IP GEOLOCATION")
print(Fore.WHITE + "=============================================")
print(Fore.BLUE + "Query: " + response['query'])
print("Status of retrieving data : " + response['status'])
print("Country: " + response['country'])
print("Country Code: " + response['countryCode'])
print("Region: " + response['region'])
print("Region Name: " + response['regionName'])
print("City: " + response['city'])
print("Continent: "+ response['continent'])
print(Fore.WHITE + "=============================================")
print(Fore.RED + "ISP: " + response['isp'])
print("Time Zone : " + response['timezone'])
print("Latitude: " + str(response['lat']))
print("Longitude: " + str(response['lon']))
print("Company: " + response['org'])
print("ASP: " + response['as'])
print("Hosting: " + str(response['hosting']))
print(Fore.WHITE + "=============================================")




