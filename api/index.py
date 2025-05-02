import sys, os
from flask import Flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from projects.job_tracker.app import app as tracker_app

# ——————— ADD THESE TWO LINES ———————
from projects.job_tracker.models import db
db.init_app(tracker_app)
# ————————————————————————————————

root_app = Flask("root_app")
app = DispatcherMiddleware(root_app, {
    '/api': tracker_app
})