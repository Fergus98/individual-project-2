from flask import Flask, request
from application import app
import requests
import random



@app.route('/logic', methods=['GET', 'POST'])
def post_numbers():
    #accountNumber = requests.get('http://51.132.128.111:5000/number') + requests.get('http://51.132.128.111:5000/letter')
    api = 'http://51.132.128.111:5000/number'
    response = requests.get(api + '/get/json')
    return 'Whole repsonse: ' + str(response.json())
