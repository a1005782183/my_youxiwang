from config import config_map
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_wtf import CSRFProtect

import redis
from youxiwang.utils.commons import ReConverter
from flask_socketio import SocketIO
from flask_msearch import Search

db = SQLAlchemy()
redis_store = None
socket_io = SocketIO()
search = Search()

def create_app(config_name):

	app = Flask(__name__)	

	config_class = config_map.get(config_name)
	app.config.from_object(config_class)

	db.init_app(app)

	global redis_store
	redis_store = redis.StrictRedis(host=config_class.REDIS_HOST, port=config_class.REDIS_PORT)

	Session(app)

	CSRFProtect(app)

	search.init_app(app)

	# 为flask添加自定义转换器
	app.url_map.converters['re'] = ReConverter

	# 注册提供静态文件的蓝图
	from youxiwang import web_html
	app.register_blueprint(web_html.html)
	
	# 注册蓝图
	from youxiwang import yxw_app
	app.register_blueprint(yxw_app.api)
	
	socket_io.init_app(app)
	return app