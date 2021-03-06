import os
from flask import Flask
from flask.ext.cors import CORS

DATABASE = os.getenv("DATABASE_URL", 
    "postgresql://postgres:secret@db/postgres").strip()

app = Flask(__name__)
app.config.from_object(__name__)
CORS(app, resources=r'/*', allow_headers="Content-Type")

import todo.views
