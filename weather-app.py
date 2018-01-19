import urllib.request
import json
from sys import argv
import pprint

url = "http://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b6907d289e10d714a6e88b30761fae22"
req = urllib.request.urlopen(url)
data = req.read()
parsedData = json.loads(data)
pprint.pprint(parsedData)

