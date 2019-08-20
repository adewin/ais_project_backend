# 使用 flask_restful 模块
from flask import Blueprint, request, jsonify
from flask_restful import reqparse, Api, Resource, abort
from datetime import datetime
from sqlalchemy import and_, or_
from App.Models.models import ShipInfo, Pos
from App.Controllers.calc import dbscan_calc,dbscan_bmap, KNN
from App.Controllers.tools import intToCoordinate, CoordinateToInt

clustering_analysis_api = Blueprint('clustering_analysis', __name__)
clustering = Api(clustering_analysis_api)

# 计算K-Dist,结果返回到前端生成echarts图
# 一天内的数据计算量过大，默认使用一天内某一段时间范围作为测试数据
class calcKDist(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('top', type=str, required=True)
        self.parser.add_argument('bottom', type=str, required=True)
    def get(self):
        args = self.parser.parse_args()
        point1 = args['top']
        point2 = args['bottom']
        stime = '20170809 16:00'
        etime = '20170809 16:10'
        point1_lng = CoordinateToInt(point1.split(',')[0])
        point1_lat = CoordinateToInt(point1.split(',')[1]) 
        point2_lng = CoordinateToInt(point2.split(',')[0]) 
        point2_lat = CoordinateToInt(point2.split(',')[1])
        points_list = []
        pos = Pos.query.filter(and_(Pos.InsertTime >= stime, Pos.InsertTime <=etime, Pos.Lat > point2_lat, Pos.Lat < point1_lat, Pos.Lon > point1_lng, Pos.Lon < point2_lng))
        for i in pos:
            point_list = [float(intToCoordinate(i.Lon)), float(intToCoordinate(i.Lat))]
            points_list.append(point_list)
        # print(points_list)
        return KNN(points_list)
        # return len(points_list)
# 计算给定矩形范围（经纬度）内所有点的DBSCAN
# 数据输出格式适用于在vue-bmap海量点组件中使用
class calcDbscanByRectangle(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('task', type=str)
        self.parser.add_argument('lnglat_top_left', type=str, required=True)
        self.parser.add_argument('lnglat_bottom_right', type=str, required=True)
        self.parser.add_argument('eps', type=int, required=True)
        self.parser.add_argument('minpts', type=int, required=True)
    def post(self):
        args = self.parser.parse_args()
        point1 = args['lnglat_top_left']
        point2 = args['lnglat_bottom_right']
        eps = args['eps']
        minpts = args['minpts']
        point1_lng = CoordinateToInt(point1.split(',')[0])
        point1_lat = CoordinateToInt(point1.split(',')[1]) 
        point2_lng = CoordinateToInt(point2.split(',')[0]) 
        point2_lat = CoordinateToInt(point2.split(',')[1])

        points_list = []
        pos = Pos.query.filter(and_(Pos.Lat > point2_lat, Pos.Lat < point1_lat, Pos.Lon > point1_lng, Pos.Lon < point2_lng))
        for i in pos:
            point_list = [intToCoordinate(i.Lon), intToCoordinate(i.Lat)]
            points_list.append(point_list)

        res = dbscan_bmap(points_list, eps, minpts)
        return res

clustering.add_resource(calcKDist, '/calc_kdist_by_rectangle/')
clustering.add_resource(calcDbscanByRectangle, '/calc_dbscan_by_rectangle')
