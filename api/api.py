import warnings
from flask import Flask, jsonify, request, abort, json
from flask_jwt_extended import JWTManager
from flask_cors import cross_origin
import pymysql
import json
import os
from dotenv import load_dotenv
import logging
import db
warnings.filterwarnings("ignore")


app = Flask(__name__)


@app.route('/api/v1.0/get_rew_log', methods=['GET'])
def get_rew_log():
    data = db.get_rew_log()
    response = app.response_class(
        response=json.dumps(data, default=str),
        status=200,
        mimetype='application/json'
    )
    print(response, "__________")
    return response


@app.route('/api/v1.0/create_rewlog', methods=['POST'])
def create_rew_log():
    data = db.create_rew_log()
    response = app.response_class(
        response=json.dumps(data, default=str),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/api/v1.0/get_ErrorLog', methods=['GET'])
def get_ErrorLog():
    data = db.get_ErrorLog()
    response = app.response_class(
        response=json.dumps(data, default=str),
        status=200,
        mimetype='application/json'
    )
    print(response, "__________")
    return response

@app.route('/api/v1.0/create_ErrorLog', methods=['POST'])
def create_ErrorLog():
    data = db.create_ErrorLog()
    response = app.response_class(
        response=json.dumps(data, default=str),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/')
@cross_origin()
def hello_world():
  
    data = db.get_hello_world()
    response = app.response_class(
        response=json.dumps(data, default=str),
        status=200,
        mimetype='application/json'
    
    )
    return response
    

if __name__ == '__main__':
    app.run(debug=False)