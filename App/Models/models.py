from App.ext import db

# 船舶信息模型
class ShipInfo(db.Model):
    mmsi = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.Integer)
    shipType = db.Column(db.Integer)
    shipName = db.Column(db.String)
    Length = db.Column(db.Integer)
    Width = db.Column(db.Integer)
    Left = db.Column(db.Integer)
    Trail = db.Column(db.Integer)

# 船舶信息模型(去重后)
class ShipInfoSet(db.Model):
    ROWID = db.Column(db.Integer, primary_key=True)
    mmsi = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.Integer)
    shipType = db.Column(db.Integer)
    shipName = db.Column(db.String)
    Length = db.Column(db.Integer)
    Width = db.Column(db.Integer)
    Left = db.Column(db.Integer)
    Trail = db.Column(db.Integer)
    Draught = db.Column(db.Integer)
    IMO = db.Column(db.Integer)
    callSign = db.Column(db.Integer)
    Dest = db.Column(db.String)
    UpdateTime= db.Column(db.Integer)
    InsertTime = db.Column(db.DateTime)
# class Test(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     time = db.Column(db.DateTime)

# AIS点信息模型
class Pos(db.Model):
    ROWID = db.Column(db.Integer, primary_key=True)
    mmsi = db.Column(db.Integer)
    source = db.Column(db.Integer)
    Lat = db.Column(db.Integer)
    Lon = db.Column(db.Integer)
    Sog = db.Column(db.Integer)
    Cog = db.Column(db.Integer)
    Hdg = db.Column(db.Integer)
    Rot = db.Column(db.Integer)
    Navastaus = db.Column(db.Integer)
    UpdateTime= db.Column(db.Integer)
    InsertTime = db.Column(db.DateTime)