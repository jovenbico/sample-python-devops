import os
import logging

from slack_sdk import WebClient

logging.basicConfig(level=logging.DEBUG)

# TODO (Developer)
# Set the SLACK_BOT_TOKEN environment variable

SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
client = WebClient(token=SLACK_BOT_TOKEN)
res = client.api_test()