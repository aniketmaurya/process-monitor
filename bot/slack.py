import json
import os
from dotenv import load_dotenv
from slack_sdk import WebClient

path = os.path.dirname(__file__)
load_dotenv()
with open(f"{path}/../configs/slack_conf.json", "r") as fr:
    slack_conf = json.loads(fr.read())

slack_token = os.environ["SLACK_BOT_TOKEN"]
channel = slack_conf["channel"]
client = WebClient(token=slack_token)


def post_msg(text):
    return client.chat_postMessage(channel=channel, text=text)
