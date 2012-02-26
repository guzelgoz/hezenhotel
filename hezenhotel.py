# -*- coding: utf-8 -*-
"""
    Hezen Hotel Website
    ~~~~~~~~~~~~~~

    A simple hotel website

    :copyright: (c) 2012 by Hakan Guzelgoz.
    :license: BSD, see LICENSE for more details.
"""
import os
from flask import Flask, jsonify, render_template, request, abort, g, flash
from flaskext.markdown import Markdown
import yaml

app = Flask(__name__)
md = Markdown(app, extensions = ['codehilite'])

@app.route('/')
def index():
	post = yaml.load(file('index.yaml', 'r'))
	return render_template('index.html', post=post )

@app.route('/rooms')
def rooms():
	post = yaml.load(file('rooms.yaml', 'r'))
	return render_template('content.html', post=post )
	
	
if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)