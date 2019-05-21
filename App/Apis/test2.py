# 使用 flask_restful 模块
from flask import Blueprint, request, jsonify
from flask_restful import reqparse, Api, Resource, abort
# from App.ext import db

test2 = Blueprint('api2', __name__)
api_test2= Api(test2)

class Hello(Resource):
    def get(self):
        return {'hello': 'world'}

class getParameters(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('start', type=str)
        self.parser.add_argument('end', type=str)
    def get(self):
        data = self.parser.parse_args()
        val1 = data.get('start')
        val2 = data.get('end')
        return {'s': val1, 'e': val2}

api_test2.add_resource(Hello, '/test2')
api_test2.add_resource(getParameters, '/get_parameters/')