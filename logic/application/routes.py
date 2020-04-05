from flask import Flask, request
from application import app
import requests
import random



@app.route('/logic', methods=['GET', 'POST'])
def post_numbers():
    #accountNumber = requests.get('http://51.132.128.111:5000/number') + requests.get('http://51.132.128.111:5000/letter')
    api = 'http://numbers:5003/number'
    api2 = 'http://letters:5002/letter'
    response = requests.get(api)
    response1 = requests.get(api2)
    accountNumber = str(response.text) + str(response1.text)
    return accountNumber
