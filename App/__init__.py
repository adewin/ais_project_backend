from flask import Flask
from flask_cors import CORS
from App.ext import init_ext
from App.settings import envs

# 蓝图注册
def register_bps(app):
    from App.Apis.test import test
    from App.Apis.test_data import test_data
    from App.Apis.dbscan_api import dbscan_api
    from App.Apis.basic_query import basic_query_api
    app.register_blueprint(test, url_prefix='/api')
    app.register_blueprint(test_data, url_prefix='/api')
    app.register_blueprint(basic_query_api, url_prefix='/api')
    app.register_blueprint(dbscan_api)


# 创建和配置应用
def create_app():
    app = Flask(__name__, template_folder=settings.TEMPLATE_FOLDER)

    app.config.from_object(envs.get('postgreConfig'))
    
    register_bps(app)

    init_ext(app)

    CORS(app, supports_credentials=True)

    return app