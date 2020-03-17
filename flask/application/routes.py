from flask import Flask, request
from application import app
import random



@app.route('/home', methods=['GET'])
def post_numbers():
        response = requests.get(api + '')
	return render_template('home.html', title='Home')
