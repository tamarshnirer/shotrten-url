from flask import Flask, render_template, request, redirect, url_for
import json
import string
import random

app = Flask(__name__)

# Load existing URLs from the JSON file if it exists
try:
    with open('urls.json') as file:
        urls = json.load(file)
except FileNotFoundError:
    urls = {}

def generate_short_url():
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for _ in range(6))
    return short_url

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        long_url = request.form.get('long_url')
        short_url = generate_short_url()
        urls[short_url] = long_url

        # Save the URL mapping to a JSON file
        with open('urls.json', 'w') as file:
            json.dump(urls, file)

        return render_template('index.html', short_url=request.host_url + short_url)
    return render_template('index.html')

@app.route('/<short_url>')
def redirect_to_long_url(short_url):
    long_url = urls.get(short_url)
    if long_url:
        return redirect(long_url)
    return '<h1>URL not found</h1>'

if __name__ == '__main__':
    app.run(debug=True)