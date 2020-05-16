from flask import Flask

app = Flask(__name__)

from . import banker_route
