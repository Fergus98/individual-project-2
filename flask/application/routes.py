from flask import Flask, request
from application import app
import requests
import random



@app.route('/home', methods=['GET'])
def post_numbers():
	return render_template('home.html', title='Home')
