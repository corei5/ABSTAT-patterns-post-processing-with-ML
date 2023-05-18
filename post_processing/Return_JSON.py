import json
import requests

def return_JSON(abstat_id):
    url = "http://backend.abstat.disco.unimib.it/api/v1/browse?enrichWithSPO=true&summary=" + abstat_id + "&subj=&pred=&obj=&offset=0"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    json_object = json.loads(response.text)
    return json_object
