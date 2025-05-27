from flask import render_template, request, redirect, session
from app import app

@app.route('/auth')
def auth():
    render_template('auth.html')
