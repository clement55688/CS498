import requests
import json
import uuid

url = "https://seorwrpmwh.execute-api.us-east-1.amazonaws.com/prod/mp3-lexv2-autograder"

payload = {
	"graphApi": "https://3a3kptzaue.execute-api.us-east-1.amazonaws.com/mp3/graph",
	"botId": "KDMSFJMFVZ",
	"botAliasId": "TSTALIASID",
	"identityPoolId": "us-east-1:23c8b308-11d4-4240-905d-dfa918b01589",
	"accountId": "471112527243",
	"submitterEmail": "cl154@illinois.edu",
	"secret": "CvKsYEzdI9L8uMwQ",
	"region": "us-east-1"
    }

r = requests.post(url, data=json.dumps(payload))

print(r.status_code, r.reason)
print(r.text)