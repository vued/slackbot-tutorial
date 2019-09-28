import os
import logging

if __name__ == "__main__":
  os.environ['SLACK_BOT_TOKEN'] = 'xoxb-3538498893-779033090182-5c0R6igZboAGVBYdBCvh41nJ'
  logging.debug("set slack bot token")
  print ('Token set to ' + os.environ['SLACK_BOT_TOKEN'])
  