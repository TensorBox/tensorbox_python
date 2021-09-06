import requests, json
api_key = None
URL = 'https://api.tensorbox.ai'

class Client:
    @staticmethod
    def generate(payload):
        if api_key == None:
            raise Exception("API key has to be defined")
        payload['uid'] = api_key 
        res = requests.post(URL+"/api/get_prediction", json=payload)
        if res.status_code == 200:
            return json.loads(res.text)
        else:
            raise Exception(res.text)
