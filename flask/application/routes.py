from flask import Flask, request
from application import app
import random



@app.route('/home', methods=['GET'])
def post_numbers():
    api3 = 'http://51.132.128.111:5001/logic'
    response3 = requests.get(api3)
    return render_template('home.html', title='Home')
