#!/usr/bin/python3
"""Flask application demonstrating Jinja loops and conditionals."""
import json
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')


@app.route('/about')
def about():
    """Render the about page."""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Render the contact page."""
    return render_template('contact.html')


@app.route('/items')
def items():
    """Render the items page with data loaded from a JSON file."""
    with open('items.json') as f:
        data = json.load(f)
    return render_template('items.html', items=data['items'])


if __name__ == '__main__':
    app.run(debug=True, port=5000)
