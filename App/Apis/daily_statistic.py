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


class getDailyStatistic(Resource):
    def get(self):
        # ship = ShipInfoSet.query.all()
        # number = 0
        # detail = []
        # hourdict = {
        #     '01':0,'02':0,'03':0,'04':0,'05':0,'06':0,'07':0,'08':0,'09':0,'10':0,'11':0, '12':0,'13':0,
        #     '14':0,'15':0,'16':0,'17':0,'18':0, '19': 0, '20': 0, '21':0,'22': 0,'23':0,'00': 0
        # }
        # for i in ship:
        #     number += 1
        #     update = timestampToDatetime(i.UpdateTime, format='sec')[11:13].strip()
        #     hour = i.InsertTime.strftime('%Y-%m-%d %H:%M:%S')[11:13].strip()

        #     for h in hourdict:
        #         # print('字典', h, type(h))
        #         if h == update:
        #             # print('加一')
        #             hourdict[h] += 1
        #         else:
        #             pass
        # return hourdict
        return {
            "10": 6600,
            "11": 5286,
            "12": 4883,
            "13": 4315,
            "14": 4039,
            "15": 4163,
            "16": 18756,
            "17": 8571,
            "18": 9179,
            "19": 9020,
            "20": 10430,
            "21": 8097,
            "22": 7241,
            "23": 1847,
            "01": 2110,
            "02": 2014,
            "03": 1345,
            "04": 331,
            "05": 348,
            "06": 544,
            "07": 2767,
            "08": 7525,
            "09": 8088,
            "00": 721
        }
class getDailyShiptype(Resource):
    def get(self):
        ship = ShipInfoSet.query.all()
        number = 0
        detail = []
        typedict = {
            '50': 0,'51':0,'52':0,'53':0,'54':0,'55':0,'56':0,'57':0,'58':0,'59':0,'30':0,'31':0,'32':0,
            '33':0,'34':0,'35':0,'36':0,'37':0, '2*':0, '4*':0,'6*':0,'7*':0,'8*':0
        }
        for i in ship:
            shiptype = i. shipType
            Upship = shiptype / 10
            for t in typedict:

                if int(t[0:1]) == 3 or int(t[0:1]) == 5:
                    if int(t) == shiptype:
                        typedict[t] += 1
                    else:
                        pass
                elif int(t[0:1]) == Upship:
                    typedict[t] += 1
                else:
                    # typedict['0'] += 1
                    pass
        return typedict

class getShipType(Resource):
    def get(self):
        data = [
            { 'name': "捕捞", 'value': 8608 },
            { 'name': "拖引", 'value': 159 },
            { 'name': "疏浚或水下作业", 'value': 725 },
            { 'name': "潜水作业", 'value': 92 },
            { 'name': "参与军事行动", 'value': 870 },
            { 'name': "帆船航行", 'value': 404 },
            { 'name': "娱乐船", 'value': 1395 },
            { 'name': "引航船", 'value': 560 },
            { 'name': "搜救船", 'value': 460 },
            { 'name': "拖轮", 'value': 4560 },
            { 'name': "港口供应船",'value': 219 },
            { 'name': "装有防污设备的船舶",'value': 144 },
            { 'name': "执法船", 'value': 451 },
            { 'name': "备用船", 'value': 285 },
            { 'name': "医疗船", 'value':38 },
            { 'name': "地效应船", 'value': 154 },
            { 'name': "高速船", 'value': 563 },
            { 'name': "客船", 'value': 2831 },
            { 'name': "货船", 'value': 32813 },
            { 'name': "邮轮",'value': 7159 }
        ]
        return data

daily_statistic.add_resource(getDailyStatistic, '/get_daily_statistic/')
daily_statistic.add_resource(getDailyShiptype, '/get_daily_shiptype/')
daily_statistic.add_resource(getShipType, '/get_shiptype/')
