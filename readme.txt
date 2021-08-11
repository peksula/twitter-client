# Prerequites
- Python (developed and tested to work with python 3.8)
- Pip

# Install required libraries from PyPi
'pip install -r requirements.txt'

# How to run
- Run main.py with Python. It just starts the webserver.
- Once the server is running, point your webbrowser to http://127.0.0.1:5000/

# Design
- Project consists of backend webserver implementation and a frontend web application
  - 3rd party Flask framework implements the actual web server
  - Frontend is built with Jinja templating engine. Jinja makes it possible to write python
    code within HTML. When the web browser requests the web page, the page is dynamically
    created by it (in the webserver context) and once ready sent to the browser.
  - The web pages access Twitter via Tweepy python Twitter client.

- Webserver.py responds to requests send by the web browser
  - Each supported 'entry point' has a separate 'route' registered and implemented
    - For example http://127.0.0.1/tweets maps to route '/tweets'
    - Server asks Jinja templating engine to render the webpage in question, supplying the
      authenticated twitter client for fetching content from Twitter itself

- Auth.py
  - Abstracts the Tweepy's authentication handler. We are using OAuth1 authentication.
    We ask user to authenticate the application to access Twitter as herself.

- Main.py
  - Application entry point. Starts the webserver.

- Twitter.py
  - The Twitter access implementation.