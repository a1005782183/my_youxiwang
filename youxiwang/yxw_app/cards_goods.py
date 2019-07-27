from . import api
from youxiwang.models import cards, card_bag, middle, User
import json
from flask import jsonify, session, request
from youxiwang import db, redis_store

@api.route("/goods/<int:page>/<search>")
def get_goods_data(page,search):
	'''获取所有卡牌数据'''
	
	if not page:
		page = 1
	if search == "undefined":
		search = "all"

	# 搜索
	if search != "all":
		card = cards.query.msearch(search,fields=['name']).paginate(page=page, per_page=12)
	else:
		card = cards.query.order_by().paginate(page=page, per_page=12)
	card_item = card.items
	cards_lis = []
	iter_pages=[]
	
	for i in card.iter_pages():
		iter_pages.append(i)

	for c in card_item:
		cards_lis.append(c.to_dict())

	# 控制分页
	if page <= 5:
		iter_pages = iter_pages[page-1:page+4]
	elif page == iter_pages[-2] or page == iter_pages[-1]:
		iter_pages = iter_pages[-3:]
	elif page >= iter_pages[-4]:
		iter_pages = iter_pages[-5:]
	else:
		iter_pages = iter_pages[4:9]

	data_dict = dict(data=cards_lis, has_prev=card.has_prev, has_next=card.has_next, iter_pages=iter_pages,
		prev_num=card.prev_num, next_num=card.next_num)
	data = json.dumps(data_dict)

	return data, 200, {"Content-Type": "application/json"}

@api.route("/detail/<int:id>")
def show_detail(id):
	'''详情页数据'''

	card = cards.query.filter_by(id=id).first()

	data = json.dumps(card.to_dict())

	return data, 200, {"Content-Type": "application/json"}


@api.route("/add_card/<int:id>")
def add_card(id):
	"""添加卡牌到卡包"""

	# 判断用户是否已登录
	username = session.get("username")
	if username is None:
		return jsonify(errno=1, errmsg="请先登录")
	# 获取用户id
	user = User.query.filter_by(username=username).first()
	# 删除商品数据缓存
	redis_data = redis_store.delete("card_group_%s" % user.id)

	# 插入用户id到卡包
	try:
		bag = card_bag(user_id=user.id)

		db.session.add(bag)
		db.session.commit()

		# 卡包和卡牌插入中间表
		mid = middle(cards_id=id, card_bag_id=bag.id)
	
		db.session.add(mid)
		db.session.commit()
	except:
		db.session.rollback()
		return jsonify(errno=1, errmsg="查询数据库异常")
	flask_whooshalchemyplus.index_one_model(cards)

	return jsonify(errno=0, errmsg="添加成功")