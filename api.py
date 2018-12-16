import requests
import json


class Api:
    def __init__(self, user_input):
        self.url = "https://api.jdoodle.com/v1/execute"
        self.headers = {'Content-type': 'application/json'}
        self.payload = {"clientId": "561d4b78be8ac77f9711aa827bb661c6",
                        "clientSecret": "5cadd43a0f7f4c187f428be50af70ef6bba434db749975e21598cbd4b01e2139",
                        "script": """{}""".format(user_input),
                        "language": "c",
                        "versionIndex": "3",
                        }
        self.response = requests.post(url=self.url, data=json.dumps(self.payload), headers=self.headers)
        self.finalstring = self.response.json()

