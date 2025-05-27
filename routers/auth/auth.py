from flask import render_template, request, redirect, session
from app import app

@app.route('/')
def auth():
    return render_template('auth.html')
