# 使用 flask_restful 模块
from flask import Blueprint, request, jsonify
from flask_restful import reqparse, Api, Resource, abort
from datetime import datetime
from sqlalchemy import and_, or_
from App.Models.models import Pos, ShipInfoSet
from App.Controllers.calc import dbscan_calc,dbscan_bmap
from App.Controllers.tools import intToCoordinate, CoordinateToInt

test_data = Blueprint('test_data', __name__)
api_data= Api(test_data)



class getData(Resource):
    def get(self):
        shipinfo = ShipInfoSet.query.filter_by(mmsi=98506108)
        infos = []
        for i in shipinfo:
            info = {}
            info.update(mmsi=i.mmsi, source=i.source, shipType=i.shipType)
            infos.append(info)
        return {'info': infos}

class getPos(Resource):
    def get(self):
        # pos = Pos.query.filter_by(updatetime=1502354830)
        pos = Pos.query.filter_by(mmsi=235070199)
        data = []
        for i in pos:
            info = {}
            info.update(id=i.ROWID,mmsi=i.mmsi, source=i.source, lat=intToCoordinate(i.Lat), lon=intToCoordinate(i.Lon), sog=i.Sog,cog=i.Cog, hdg=i.Hdg, rot=i.Rot, navastaus=i.Navastaus, updatetime=i.UpdateTime)
            info.update(inserttime=i.InsertTime.strftime('%Y-%m-%d %H:%M:%S'))
            data.append(info)
        return {'pos': data}

# 根据mmsi选取数据
class getLnglatByMmsi(Resource):
    def get(self):
        pos = Pos.query.filter_by(mmsi=431008147)
        lnglat = []
        for i in pos:
            lng = intToCoordinate(i.Lon)
            lat = intToCoordinate(i.Lat)
            info = {'lng': lng, 'lat': lat}
            lnglat.append(info)
        # return {'mmsi': pos[1].mmsi, 'lnglat': lnglat}
        return [{'value': 1, 'lnglat': lnglat}]





api_data.add_resource(getData, '/get_data')
api_data.add_resource(getPos, '/get_pos')
api_data.add_resource(getLnglatByMmsi, '/get_lnglat_by_mmsi')
# api_data.add_resource(getDataByLnglat, '/get_data_by_lnglat')

