import json
from flask import request, session, jsonify
from youxiwang.models import User, middle, cards
from . import api
from random import shuffle
from sqlalchemy import not_
from youxiwang import redis_store


@api.route("/check_bag")
def check_bag():
	'''查询卡组数量'''
	
	username = session.get("username")

	if not username:
		return jsonify(errno=1, errmsg="请先登录")

	user = User.query.filter_by(username=username).first()

	# 有缓存就直接返回
	redis_data = redis_store.get("card_group_%s" % user.id)

	if redis_data:
		print("缓存")
		return redis_data.decode(), 200, {"Content-Type":"application/json"}

	bag = []
	for i in user.card_bag_id:
		bag.append(middle.query.filter_by(card_bag_id=i.id).first())
	# 添加卡组
	card = []
	# 添加融合卡组
	fuse = []
	for i in bag:
		b = cards.query.filter_by(id=i.id).filter(not_(cards.card_type.like('%融合%'))).first() # 卡组
		n = cards.query.filter_by(id=i.id).filter(cards.card_type.like('%融合%')).first() # 融合卡
		if n is not None:
			fuse.append(n.to_dict())
		if b is not None:
			card.append(b.to_dict());

	# 打乱卡牌
	shuffle(card)	
	c_dict = dict(card=card, fuse=fuse)
	data = json.dumps(c_dict)

	redis_store.setex("card_group_%s" % user.id, 12000, data)

	return data, 200, {"Content-Type":"application/json"}


@api.route("/fund_card")
def fund_card():
	'''获取手牌卡牌信息'''
	card_id = request.args.get("card_id")
	card = cards.query.filter_by(id=card_id).first()
	data = json.dumps(card.to_dict())	
	return data, 200, {"Content-Type":"application/json"}

