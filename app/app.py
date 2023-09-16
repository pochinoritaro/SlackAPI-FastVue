from os import getenv

from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

load_dotenv("./data/env/.env")

app = App(token=getenv("SLACK_BOT_TOKEN"))
"""
@app.message("hello")
def say_hello(message, say):
    say(f"<@{message}> Hello, World.")
"""
if __name__ == "__main__":
    print(getenv("SLACK_BOT_TOKEN"))
    SocketModeHandler(app, getenv("SLACK_BOT_TOKEN")).start()
