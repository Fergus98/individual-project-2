from flask import Flask, request
from application import app
import random



@app.route('/number', methods=['GET', 'POST'])
def post_numbers():
    numbergen = random.randint(0000,9999)
    return str(numbergen)
