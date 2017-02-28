import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello Mark. How\'s it going?'

app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
