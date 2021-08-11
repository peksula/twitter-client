"""
Webserver.
"""
from flask import Flask, render_template, redirect, request

import twitter
from auth import auth_handler

def twitter_factory(authenticator):
    """ Closure for providing one shared twitter client instance.
        Using closure (good) instead of global variable (bad)."""
    client = None

    def _client():
        """ Creates and setups the twitter client if not already done."""
        nonlocal client
        if not client:
            client = twitter.Twitter(authenticator)
        return client

    return _client # return the function that returns the client

def create_flask_app():
    app = Flask(__name__)
    authenticator = auth_handler()

    @app.route('/callback')
    def callback():
        """ After user has authenticated in Twitter she is redirected to this endpoint."""
        # Grap the authentication verifier code from the incoming HTTP request (sent by Twitter)
        oauth_verifier = request.args.get('oauth_verifier')
        # Exchange the request token for authorized access token
        authenticator.get_access_token(oauth_verifier)
        # Now we have authenticated access to Twitter for the user

        # Render the web page to UI
        return render_template('callback.html', twitter=twitter_factory(authenticator)())

    @app.route('/tweets')
    def tweets():
        return render_template('tweets.html', twitter=twitter_factory(authenticator)())

    @app.route('/')
    def index():
        """ The root route: /.
            Redirects the user to Twitters authentication endpoint: https://api.twitter.com/oauth/.
            From there user is later redirected to /callback (handled above) """
        return redirect(authenticator.get_authorization_url())

    return app
