# 基本查询功能接口模块(统计分析)
from flask import Blueprint, request, jsonify
from flask_restful import reqparse, Api, Resource, abort
import datetime, time
import json
from App.ext import db
from sqlalchemy import and_, or_
from App.Models.models import ShipInfoSet
from App.Controllers.tools import intToCoordinate, CoordinateToInt, timestampToDatetime

daily_statistic_api = Blueprint('daily_statistic', __name__)
daily_statistic = Api(daily_statistic_api)

# class queryShipByMMSI(Resource):
#     def __init__(self):
#         self.parser = reqparse.RequestParser()
#         self.parser.add_argument('MMSI', type=str, required=True)
#     def post(self):
#         args = self.parser.parse_args()
#         mmsi = args['MMSI']
#         ship = ShipInfoSet.query.filter_by(mmsi = mmsi)

#         detail = []
#         for i in ship:
#             info = {}
#             info.update(id=i.ROWID, mmsi=i.mmsi, source=i.source, shiptype=i.shipType, shipname=i.shipName, length=i.Length, 
#             width=i.Width, left=i.Left, trail=i.Trail, draught=i.Draught, imo=i.IMO, callsign=i.callSign, dest=i.Dest)
#             info.update(updatetime=timestampToDatetime(i.UpdateTime, format='sec'))
#             info.update(inserttime=i.InsertTime.strftime('%Y-%m-%d %H:%M:%S'))
#             detail.append(info)

#         return [{'detail': detail}]

class getDailyStatistic(Resource):
    def get(self):
        ship = ShipInfoSet.query.all()
        number = 0
        detail = []
        # hourList = [no16, no17, no18, no19, no20, no21, no22, no23, no24]
        hourdict = {
            '01':0,'02':0,'03':0,'04':0,'05':0,'06':0,'07':0,'08':0,'09':0,'10':0,'11':0, '12':0,'13':0,
            '14':0,'15':0,'16':0,'17':0,'18':0, '19': 0, '20': 0, '21':0,'22': 0,'23':0,'00': 0
        }


        for i in ship:
            number += 1
            update = timestampToDatetime(i.UpdateTime, format='sec')[11:13].strip()
            hour = i.InsertTime.strftime('%Y-%m-%d %H:%M:%S')[11:13].strip()
            # print('船舶', hour, type(hour))
            for h in hourdict:
                # print('字典', h, type(h))
                if h == update:
                    # print('加一')
                    hourdict[h] += 1
                else:
                    pass
            # print(hourdict)
            # info = {}
            # info.update(hour=hour)
            # detail.append(info)
            # info.update(id=i.ROWID, mmsi=i.mmsi, source=i.source, shiptype=i.shipType, shipname=i.shipName, length=i.Length, 
            # width=i.Width, left=i.Left, trail=i.Trail, draught=i.Draught, imo=i.IMO, callsign=i.callSign, dest=i.Dest)
            # info.update(updatetime=timestampToDatetime(i.UpdateTime, format='sec'))
            # info.update(inserttime=i.InsertTime.strftime('%Y-%m-%d %H:%M:%S'))
            # detail.append(info)
        
        return hourdict

daily_statistic.add_resource(getDailyStatistic, '/get_daily_statistic/')