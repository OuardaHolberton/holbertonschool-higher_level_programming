#!/usr/bin/python3
"""Flask application demonstrating reading data from JSON, CSV, or SQLite."""
import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json():
    """Read and return product data from the JSON file."""
    with open('products.json') as f:
        return json.load(f)


def read_csv():
    """Read and return product data from the CSV file."""
    products = []
    with open('products.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price'])
            })
    return products


def read_sql():
    """Read and return product data from the SQLite database."""
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, category, price FROM Products')
    rows = cursor.fetchall()
    conn.close()

    products = []
    for row in rows:
        products.append({
            'id': row[0],
            'name': row[1],
            'category': row[2],
            'price': row[3]
        })
    return products


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


@app.route('/products')
def products():
    """Render product data from JSON, CSV, or SQL, optionally by id."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ('json', 'csv', 'sql'):
        return render_template(
            'product_display.html', error="Wrong source"
        )

    try:
        if source == 'json':
            data = read_json()
        elif source == 'csv':
            data = read_csv()
        else:
            data = read_sql()
    except Exception:
        return render_template(
            'product_display.html', error="Error reading data source"
        )

    if product_id is not None:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template(
                'product_display.html', error="Product not found"
            )

        filtered = [p for p in data if p['id'] == product_id]
        if not filtered:
            return render_template(
                'product_display.html', error="Product not found"
            )
        data = filtered

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
