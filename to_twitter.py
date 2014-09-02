from os import environ
from time import sleep

from twitter import Twitter
from twitter.oauth import Oauth

from tla_ound import generator


def do_auth():
  return Twitter(auth=Oauth(environ.get(token), environ.get(secret),
  environ.get(apikey), environ.get(apisecret)))
