# 基本查询功能接口模块(船舶信息)
from flask import Blueprint, request, jsonify
from flask_restful import reqparse, Api, Resource, abort
import datetime, time
from App.ext import db
from sqlalchemy import and_, or_
from App.Models.models import ShipInfoSet
from App.Controllers.tools import intToCoordinate, CoordinateToInt, timestampToDatetime

ship_query_api = Blueprint('ship_query', __name__)
ship_query = Api(ship_query_api)

# 从pos对象转换成指定格式的json结果
# num: 数据总条数， detail: 所有数据详细信息， lnglat：将每条数据的坐标转换成指定格式，方便再vue-bmap组件上显示
# def getDataFromShip(ship):
#         detail = []
#         lnglat = []
#         number = 0
#         for i in ship:
#             number += 1
#             lng = intToCoordinate(i.Lon)
#             lat = intToCoordinate(i.Lat)
#             lnglat_info = {'lng': lng, 'lat': lat}
#             lnglat.append(lnglat_info)
#             info = {}
#             info.update(id=i.ROWI0D,mmsi=i.mmsi, source=i.source, lat=intToCoordinate(i.Lat), lon=intToCoordinate(i.Lon), sog=i.Sog, cog=i.Cog, hdg=i.Hdg, rot=i.Rot, navastaus=i.Navastaus)
#             info.update(updatetime=timestampToDatetime(i.UpdateTime, format='sec'))
#             info.update(inserttime=i.InsertTime.strftime('%Y-%m-%d %H:%M:%S'))
#             detail.append(info)
#         return [{'num': number, 'detail': detail, 'lnglat': lnglat}]

class queryShipByMMSI(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('MMSI', type=str, required=True)
    def post(self):
        args = self.parser.parse_args()
        mmsi = args['MMSI']
        ship = ShipInfoSet.query.filter_by(mmsi = mmsi)

        detail = []
        for i in ship:
            info = {}
            info.update(id=i.ROWID, mmsi=i.mmsi, source=i.source, shiptype=i.shipType, shipname=i.shipName, length=i.Length, 
            width=i.Width, left=i.Left, trail=i.Trail, draught=i.Draught, imo=i.IMO, callsign=i.callSign, dest=i.Dest)
            info.update(updatetime=timestampToDatetime(i.UpdateTime, format='sec'))
            info.update(inserttime=i.InsertTime.strftime('%Y-%m-%d %H:%M:%S'))
            detail.append(info)

        return [{'detail': detail}]


ship_query.add_resource(queryShipByMMSI, '/query_ship_by_mmsi')