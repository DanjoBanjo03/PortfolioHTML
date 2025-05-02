import os
from flask import Flask
from projects.job_tracker.models import db

app = Flask(__name__)
db.init_app(app)

# (rest of the code remains unchanged)