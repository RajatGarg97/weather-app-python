import urllib.request
import json
from sys import argv
import pprint
print(argv)
url = "http://samples.openweathermap.org/data/2.5/weather?q="+argv[1]+"&appid=b6907d289e10d714a6e88b30761fae22"
req = urllib.request.urlopen(url)
data = req.read()
parsedData = json.loads(data)
#pprint.pprint(parsedData)

obtained = parsedData['main'][argv[2]]

pprint.pprint(obtained)
