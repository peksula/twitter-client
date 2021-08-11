"""
Main application entry point.
"""

import logging
from webserver import create_flask_app

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)

# Create and run the webserver
webserver = create_flask_app()
webserver.run()
