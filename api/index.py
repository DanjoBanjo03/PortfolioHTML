import sys
import os
from flask import Flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware

# Ensure the repo root is on the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

# Import the configured Flask app from your tracker project
from projects.job_tracker.app import app as tracker_app

# Create a root app to mount under
root_app = Flask("root_app")

# Mount the tracker app under "/api", stripping that prefix before dispatch
app = DispatcherMiddleware(root_app, {
    '/api': tracker_app
})