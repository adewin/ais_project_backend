# 未使用 flask_restful 模块
from flask import Blueprint, request, jsonify
# from App.ext import db

test = Blueprint('api', __name__)

# def init_blue(app):
#     app.register_blueprint(blueprint=api)

@test.route('/test')
def index():
    return 'hello test'