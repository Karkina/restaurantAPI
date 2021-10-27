# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 11:28:31 2021

@author: nicos
"""
from flask import Flask, jsonify,request
import requests
from Site import Site

app = Flask(__name__)
app.config["DEBUG"] = False

site = Site()

@app.route('/', methods=['GET'])
def home():
    return "<h1> Mon ApI </h1>"

@app.route('/siteId', methods=['GET'])
def getId():
     id = request.args.get("id")
     
     return jsonify(site.getSiteById(id))
 
@app.route('/search', methods=['GET'])
def search():
     text = request.args.get("text")
     
     return jsonify(site.getSiteByNameContains(text))
app.run()