from youxiwang.models import User
from flask import jsonify, request, session
from . import api
from youxiwang import db
from sqlalchemy.exc import IntegrityError

@api.route("/register", methods=["POST"])
def register():
	'''注册'''

	# 获取数据
	req_json = request.get_json()

	username = req_json.get("username")
	password = req_json.get("password")

	# 判断数据完整性
	if not all([username, password]):
		jsonify(errno=1, errmsg="数据不完整")

	user = User(username=username, password=password)

	try:
		db.session.add(user)
		db.session.commit()
	except IntegrityError as e:
		# 数据库操作错误后的回滚
		db.session.rollback()
		return jsonify(errno=1, errmsg="用户已存在")
	except Exception as e:
		db.session.rollback()
		return jsonify(errno=1, errmsg="查询数据库异常")

	return jsonify(errno=0, errmsg="注册成功")


@api.route("/login", methods=["POST"])
def login():
	'''登录'''

	# 获取数据
	req_json = request.get_json()

	username = req_json.get("username")
	password = req_json.get("password")

	# 判断数据完整性
	if not all([username, password]):
		jsonify(errno=1, errmsg="数据不完整")

	try:
		user = User.query.filter_by(username=username, password=password).first()
	except Exception as e:
		return jsonify(errno=1, errmsg="查询数据错误")

	if user is None:
		return jsonify(errno=1, errmsg="用户查询不到")

	session["username"] = username

	return jsonify(errno=0, errmsg="登陆成功")


@api.route("/session")
def get_session():
	"""获取用户session"""

	username = session.get("username")

	if username is None:
		return jsonify(errno=1, errmsg="用户未登录")

	return jsonify(errno=0, username=username)
