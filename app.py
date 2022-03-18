from flask import Flask, render_template, request, redirect, url_for, flash
import random
import os

app = Flask(__name__)


@app.route('/')
def index():
    with open('insults.json') as f:
        insults = f.read()
    insults = insults.split('\n')
    insult = random.choice(insults)
    # return in json format
    return insult


if __name__ == '__main__':
    app.run(debug=False)