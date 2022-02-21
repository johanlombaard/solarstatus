import http.client
import json
import os
import datetime

#CLear the screen
def clear_console():
    os.system('cls')
clear_console()

#Write a string dictionary value
def show_string(dict):
    print(dict["name"] + " : " + dict["value"])

#Write a numeric dictionary value
def show_number(dict):
    print(dict["name"] + " : " + dict["value"] + " " + dict["unit"])

#Get the token
conn = http.client.HTTPSConnection("api.solarmanpv.com")
payload = json.dumps({
  "appSecret": "90925872d9185ad92294a9a4cbb91b18",
  "email": "johan.lombaard@outlook.com",
  "password": "9c1c9ffde74738b86c7c62167db4c70b29c5bfd87a336b0abd36249807c0df52"
})
headers = {
  'Content-Type': 'application/json'
}
conn.request("POST", "/account/v1.0/token?appId=202110227083012&language=en", payload, headers)
res = conn.getresponse()
data = res.read()
tokenDecoded = data.decode("utf-8")
tokenParsed = json.loads(tokenDecoded)
token = tokenParsed["access_token"]
#print("<token>" + token + "</token>")

#Get the current status
conn = http.client.HTTPSConnection("api.solarmanpv.com")
payload = json.dumps({
  "deviceSn": "2107054663"
})

headers = {
  'Content-Type': 'application/json',
  'Authorization': 'bearer ' + token
}
conn.request("POST", "/device/v1.0/currentData?appId=202110227083012&language=en&=", payload, headers)
res = conn.getresponse()
data = res.read()
dataDecoded = data.decode("utf-8")
dataParsed = json.loads(dataDecoded)

#Get the individual data elements
show_number(dataParsed["dataList"][47])
show_number(dataParsed["dataList"][19])
show_number(dataParsed["dataList"][20])
show_number(dataParsed["dataList"][26])
show_number(dataParsed["dataList"][29])
show_number(dataParsed["dataList"][39])
show_number(dataParsed["dataList"][50])

#print(sn1["key"])