import os
import schedule
import time
import logging
import slack
import slack_client

logging.basicConfig(level=logging.DEBUG)

def sendMessage(slack_client, msg):
  # make the POST request through the python slack client
  response = slack_client.chat_postMessage(channel='#test',text=msg)

  # check if the request was a success
  if response['ok'] is not True:
    logging.error(response)
  else:
    logging.debug(response)

if __name__ == "__main__":
  # SLACK_BOT_TOKEN = os.environ['SLACK_BOT_TOKEN']
  slack_client = slack.WebClient(token=os.environ['SLACK_BOT_TOKEN'])
  logging.debug("authorized slack client")

  # # For testing
  msg = "Good Evening!"
  schedule.every(60).seconds.do(lambda: sendMessage(slack_client, msg))

  # schedule.every().monday.at("13:15").do(lambda: sendMessage(slack_client, msg))
  logging.info("entering loop")

  while True:
    schedule.run_pending()
    time.sleep(5) # sleep for 5 seconds between checks on the scheduler
