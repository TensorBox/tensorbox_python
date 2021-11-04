import requests, json
#api_key = None
URL = 'https://api.tensorbox.ai'

class Client:
    api_key = None
    @classmethod
    def set_api_key(cls, key):
        cls.api_key = key

    @classmethod
    def generate(cls, payload):
        api_key = cls.api_key
        if api_key == None:
            raise Exception("API key has to be defined")
        payload['api_key'] = api_key 
        res = requests.post(URL+"/api/generate", json=payload)
        if res.status_code == 200:
            return json.loads(res.text)
        else:
            raise Exception(res.text)
