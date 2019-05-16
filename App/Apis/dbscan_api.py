# 使用 flask_restful 模块
from flask import Blueprint, request, jsonify
from flask_restful import reqparse, Api, Resource, abort
# from App.ext import db
from App.Controllers import calc

dbscan_api = Blueprint('dbscan_api', __name__)
api_dbscan= Api(dbscan_api)

class dbscan(Resource):
    def post(self):
        data_str = request.form['data_str']
        dis = float(request.form['eps'])
        min_points =  int(request.form['min_samples'])
        dbscan = calc.dbscan_calc(data_str, dis, min_points)
        # data = calc.get_data(data_str)
        return dbscan

class dbscan_by_value(Resource):
    def post(self):
        # if request.method == 'POST':
        data_str = request.form['data_str']
        dis = float(request.form['eps'])
        min_points =  int(request.form['min_samples'])
        dbscan = calc.dbscan_calc2(data_str, dis, min_points)

        return dbscan


api_dbscan.add_resource(dbscan, '/dbscan')
api_dbscan.add_resource(dbscan_by_value, '/dbscan_by_value')