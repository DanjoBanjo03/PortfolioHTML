from vercel_wsgi import make_wsgi_app
import sys
import os
# Ensure repo root is on the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

# Import the Flask app from the renamed module
from projects.job_tracker.app import app

handler = make_wsgi_app(app)