from flask import Flask
import os

app = Flask(
    __name__,
    template_folder=os.path.join(os.path.dirname(__file__), '..', 'templates'),
    static_folder=os.path.join(os.path.dirname(__file__), '..', 'static')
)

app.secret_key = "a3f5e8c2d9b74f8e9a0d1b2c3e4f5a6b"