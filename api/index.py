import sys, os
# Add repo root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

# Import the Flask app instance
from projects.job_tracker.app import app

# No need to wrap—Vercel will find `app` automatically