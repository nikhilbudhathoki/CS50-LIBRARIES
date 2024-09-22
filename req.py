import requests#we can not usd sys and arg and there is no command arguement in jupyter notebook
import sys
import json
if len(sys.argv)!=2:
    sys.exit()
response=requests.get("https://itunes.apple.com/search?term="+sys.argv[1]+"&entity=musicTrack&limit=1")
print(json.dumps(response.json(), indent=2))
