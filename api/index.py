import sys, os
from flask import Flask

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from projects.job_tracker.app import app as tracker_app

# Expose the Flask app directly for Vercel
app = tracker_app