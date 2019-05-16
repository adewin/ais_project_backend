# 基本查询功能接口模块
from flask import Blueprint, request, jsonify
from flask_restful import reqparse, Api, Resource, abort
import datetime, time
from App.ext import db
from sqlalchemy import and_, or_
from App.Models.models import ShipInfo, Pos
from App.Controllers.tools import intToCoordinate, CoordinateToInt, timestampToDatetime

basic_query_api = Blueprint('basic_query', __name__)
basic_query = Api(basic_query_api)

# 从pos对象转换成指定格式的json结果
# num: 数据总条数， detail: 所有数据详细信息， lnglat：将每条数据的坐标转换成指定格式，方便再vue-bmap组件上显示
def getDataFromPos(pos):
        detail = []
        lnglat = []
        number = 0
        for i in pos:
            number += 1
            lng = intToCoordinate(i.Lon)
            lat = intToCoordinate(i.Lat)
            lnglat_info = {'lng': lng, 'lat': lat}
            lnglat.append(lnglat_info)
            info = {}
            info.update(id=i.ROWID,mmsi=i.mmsi, source=i.source, lat=intToCoordinate(i.Lat), lon=intToCoordinate(i.Lon), sog=i.Sog, cog=i.Cog, hdg=i.Hdg, rot=i.Rot, navastaus=i.Navastaus)
            info.update(updatetime=timestampToDatetime(i.UpdateTime, format='sec'))
            info.update(inserttime=i.InsertTime.strftime('%Y-%m-%d %H:%M:%S'))
            detail.append(info)
        return [{'num': number, 'detail': detail, 'lnglat': lnglat}]

# 按入库时间InsertTime查询(每分钟区间)
# 输出结果方便显示在vue-bmap组件上
class queryByInsertTime(Resource):
    def get(self, insert_time):
        min_insert_time = insert_time + ':00'
        max_insert_time = insert_time + ':59' 
        # pos = Pos.query.filter_by(InsertTime=insert_time)
        pos = Pos.query.filter(and_(Pos.InsertTime >= min_insert_time, Pos.InsertTime <= max_insert_time))

        a = getDataFromPos(pos)
        return a

        
# 按入库时间UpdateTime查询(每分钟区间)
# (不好用，时间没有规律)
class queryByUpdateTime(Resource):
    def get(self, update_time):
        min_update_time = int(time.mktime(time.strptime(update_time + ':00', '%Y-%m-%d %H:%M:%S')))
        max_update_time = int(time.mktime(time.strptime(update_time + ':59', '%Y-%m-%d %H:%M:%S')))
        pos = Pos.query.filter(and_(Pos.UpdateTime >= min_update_time, Pos.UpdateTime <= max_update_time))

        a = getDataFromPos(pos)
        return a

# 按mmsi查询
class queryByMMSI(Resource):
    def get(self, mmsi):
        pos = Pos.query.filter_by(mmsi = mmsi)
        a = getDataFromPos(pos)
        return a 

basic_query.add_resource(queryByInsertTime, '/get_data_by_inserttime/<insert_time>')
basic_query.add_resource(queryByUpdateTime, '/get_data_by_updatetime/<update_time>')
basic_query.add_resource(queryByMMSI, '/get_data_by_mmsi/<mmsi>')


