from flask import Flask, render_template, jsonify, g, request
from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")



