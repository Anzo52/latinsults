from flask import Flask, render_template, request, redirect, url_for, flash
import random
import os
from flask_selfdoc import Autodoc

app = Flask(__name__)
auto = Autodoc(app)


@app.route('/', methods=['GET'])
@auto.doc()
def index():
    with open('insults.json') as f:
        insults = f.read()
    insults = insults.split('\n')
    insult = random.choice(insults)
    # return in json format
    return insult

@app.route('/documentation')
def documentation():
  return auto.html()

if __name__ == '__main__':
    app.run(debug=False)
