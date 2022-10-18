import requests

## single ip request
response = requests.get("http://ip-api.com/json/110.50.224.0").json()

print("Country: " + response['country'])
print("ISP: " + response['isp'])
print("Company: " + response['org'])
print("ASP: " + response['as'])
print("Latitude: " + str(response['lat']))
print("Longitude: " + str(response['lon']))
print("Region: " + response['region'])
print("Region Name: " + response['regionName'])

