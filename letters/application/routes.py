from flask import Flask, request
from application import app
import requests
import random
import string



@app.route('/letter', methods=['GET', 'POST'])
def post_numbers():
    lettergen = "".join(random.choice(string.ascii_letters) for i in range(4))
    return lettergen
