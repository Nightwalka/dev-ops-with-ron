from flask import Flask
import requests
from requests.auth import HTTPBasicAuth
import json
# creats a flask app instance
app = Flask(__name__)


@app.route("/createJIRA", methods=['POST'])
def createJIRA():
    # This code sample uses the 'requests' library:
    # http://docs.python-requests.org

  # Corrected URL
    API_TOKEN = #  Your API token

    auth = HTTPBasicAuth


    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }

    payload = json.dumps( {
    "fields": {
        "description": {
        "content": [
            {
            "content": [
                {
                "text": "This the first ticket from the API",
                "type": "text"
                }
            ],
            "type": "paragraph"
            }
        ],
        "type": "doc",
        "version": 1
        },
        
        "issuetype": {
        "id": "10003"
        },


    
        "project": {
        "key": "AUT"
        },

        "summary": "This is from Api automation",
    
    
    },
    "update": {}
    } )

    response = requests.request(
    "POST",
    url,
    data=payload,
    headers=headers,
    auth=auth
    )

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))


app.run('0.0.0.0', port=5000)