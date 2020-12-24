from apis import reddit_api
from config import reddit_config
from utils import chance
from bots.reddit.actions.posts import Posts
import time

class RedditBot():
  def __init__(self, config=reddit_config.CONFIG):
    self.api = reddit_api
    self.ready = False
    self.posts = Posts()
    self.config = config

  def _init(self):
    print(f"running as user: {self.api.user.me()}")
    self.ready = True

  def run(self):
    if self.ready:
      # log.info("running reddit bot")
      self.posts.repost(roll=self.config['chances']['post'])
    else:
      self._init()
      self.run()
      # log.info("not running reddit bot - not ready")


