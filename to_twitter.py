from os import environ
from time import sleep

from twitter import Twitter
from twitter.oauth import Oauth

from tla_ound import generator


def do_auth():
  return Twitter(auth=Oauth(environ.get("ACCESS_TOKEN"),
                            environ.get("ACCESS_SECRET"),
                            environ.get("API_KEY"),
                            environ.get("API_SECRET")))

def tweet():
  t = do_auth()
  while True:
    t.statuses.update(status=next(generator))


if __name__ == "__main__":
  tweet()
