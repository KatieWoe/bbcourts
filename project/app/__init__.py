# courtfinder/__init__.py
from flask import Flask

app = Flask(__name__)

from courtfinder.core.routes import core
app.register_blueprint(core)