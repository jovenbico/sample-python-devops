import logging
logging.basicConfig(level=logging.INFO)

import os

def post_message(message):
    from slack_sdk import WebClient
    from slack_sdk.errors import SlackApiError

    SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]

    try:
        client = WebClient(token=SLACK_BOT_TOKEN)
        response = client.chat_postMessage(
            channel='#general',
            text=message
        )
    except SlackApiError as e:
        assert e.response["error"]
        print(f"Got an error: {e.response['error']}")

if __name__ == '__main__':
    post_message('Hello, World!')