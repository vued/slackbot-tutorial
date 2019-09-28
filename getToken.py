import os
import logging

if __name__ == "__main__":
  print (os.environ['SLACK_BOT_TOKEN'])
  logging.debug("get slack bot token")