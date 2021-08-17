import json
import os
from dotenv import load_dotenv
from slack_sdk import WebClient

path = os.path.dirname(__file__)
load_dotenv()


slack_token = os.environ["SLACK_BOT_TOKEN"]
channel = os.environ["SLACK_CHANNEL"]
client = WebClient(token=slack_token)


def post_msg(text):
    return client.chat_postMessage(channel=channel, text=text)
