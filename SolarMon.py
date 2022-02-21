import http.client
import json
import os
import datetime

def clear_console():
    os.system('cls')
clear_console()

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

#Get the realtime ingo
conn = http.client.HTTPSConnection("api.solarmanpv.com")
payload = json.dumps({
  "stationId": 1576471
})

headers = {
  'Content-Type': 'application/json',
  'Authorization': 'bearer ' + token
}
conn.request("POST", "/station/v1.0/realTime", payload, headers)
res = conn.getresponse()
data = res.read()
dataDecoded = data.decode("utf-8")
dataParsed = json.loads(dataDecoded)

#Convert the last update time
lastUpdateTime = dataParsed['lastUpdateTime']
lastUpdateTimeConverted = datetime.datetime.fromtimestamp(lastUpdateTime)

#Generation power
maxGeneration = 12*455
percGeneration = round(dataParsed['generationPower'] / maxGeneration * 100, 2)

#Time difference
timeDelta = round(datetime.timedelta.total_seconds(datetime.datetime.now() - lastUpdateTimeConverted) / 60)

#Print the output
print('Power generated: \t' + str(dataParsed['generationPower']) + ' W (' + str(percGeneration) + '%)')
print('Power consumed: \t' + str(dataParsed['usePower']) + ' W')
print('Charging power: \t' + str(dataParsed['chargePower']) + ' W')
print('Discharge power: \t' + str(dataParsed['dischargePower']) + ' W')
print('Battery SoC: \t\t' + str(dataParsed['batterySoc']) + ' %')
print('Last updated: \t\t' + str(lastUpdateTimeConverted) + ' (' + str(timeDelta) + ' minutes ago)')
#print("\u2588")