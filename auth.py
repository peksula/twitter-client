"""
Authentication.
"""

import json
import logging
import tweepy

CALLBACK = 'http://localhost:5000/callback'

def _read_secrets(secrets_file):
    """ Read the API key and API secret from the x file. """
    try:
        with open(secrets_file) as x_file:
            return json.load(x_file)
    except IOError:
        logging.error('Could not read file ' + secrets_file)

def auth_handler():
    """ Returns the Tweepy OAuth handler. """
    secrets = _read_secrets('x-file.json')
    return tweepy.OAuthHandler(secrets['key'], secrets['secret'], callback=CALLBACK)
