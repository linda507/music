#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 00:35:31 2019

@author: linqingxie
"""

import nexmo
from pprint import pprint
import requests

#create a client
client = nexmo.Client(
  application_id='883b5589-c518-43e8-9eb5-3e25cdb3f25c',
  private_key='/Users/linqingxie/Downloads/private-6.key',
)

#create a Nexmo call control object
ncco = [
        {
            "action": "record",
            "eventUrl": ["http://6005143d.ngrok.io/webhooks/recordings"]
        },
        {
            "action": "talk",
            "voiceName": "Amy",
            "text": "<speak><break time='3s' />Thank you here is a song for you</speak>"
        },
        {
            "action": "stream",
            "streamUrl": [
                "https://linda507.github.io/music/Christina-Perri-A-Thousand-Years.mp3"
                ]
        }
    ]
    
#make a phone call
response = client.create_call({
  'to': [{
    'type': 'phone',
    'number': '6598240792'
  }],
  'from': {
    'type': 'phone',
    'number': '6598240792'
  },
  'ncco': ncco
})

pprint(response)

response2 = requests.get('http://6005143d.ngrok.io/webhooks/recordings')
print("response2: ", response2.status_code)

#import urllib.request, json 
#with urllib.request.urlopen("http://7885824a.ngrok.io/webhooks/recordings") as url:
 #   data = json.loads(url.read().decode())
#    print(data)

if response2.status_code == 200:
    response3 = client.get_recording(response2['recording_url'])
    pprint(response3)