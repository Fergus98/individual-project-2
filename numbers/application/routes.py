from flask import Flask, request
from application import app
import requests
import random



@app.route('/number', methods=['POST'])
def post_numbers():
	numbergen = random.randint(0000,9999)
        return numbergen 
