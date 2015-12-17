# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 15:56:28 2015

@author: hschoonjans
"""

import requests

slack_token = os.environ["SLACK_TOKEN"]
slack_endpoint = "https://slack.com/api/chat.postMessage"
slack_channel = os.environ["SLACK_CHANNEL"]
slack_username =  os.environ["SLACK_USERNAME"]
slack_emoji = os.environ["SLACK_EMOJI"]
slack_url = os.environ["SLACK_PROFILE_PIC"]
slack_message = os.environ["SLACK_MESSAGE"]

use_emoji = True
as_user = False

def post_slack_message(message, channel="#test"):
    payload = {
                'token':slack_token, 
                'channel':channel, 
                'text': message,
    }
    if as_user:
        payload['as_user']= as_user
    else:
        payload['username']= slack_username
        if use_emoji:
            payload['icon_emoji']= slack_emoji
        else:
            payload['icon_url']= slack_url
    return requests.post(slack_endpoint, params = payload)
    
response = post_slack_message(slack_message, slack_channel)