from youxiwang import db

class User(db.Model):
	"""用户表"""
	__tablename__ = "yxw_user"

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(256), unique=True, nullable=False) # 用户名
	password = db.Column(db.String(256), nullable=False) # 密码
	card_bag_id = db.relationship("card_bag") # 卡包id

class cards(db.Model):
	'''卡牌表'''

	__tablename__ = "yxw_cards"
	__searchable__ = ['name']

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(256), nullable=False) # 名称
	card_type = db.Column(db.String(256), nullable=True) # 类型
	password = db.Column(db.Integer, nullable=True) # 卡片密码
	race = db.Column(db.String(256), nullable=True) # 种族
	attribute = db.Column(db.String(256), nullable=True) # 属性
	level = db.Column(db.Integer, nullable=True) # 星级
	atk = db.Column(db.Integer, nullable=True) # 攻击力
	defend = db.Column(db.Integer, nullable=True) # 防御力
	desc = db.Column(db.String(256), nullable=True) # 描述
	img = db.Column(db.String(256), nullable=False) # 图片

	def to_dict(self):
		data = {
			'id': self.id,
			'name': self.name,
			'card_type': self.card_type,
			'password': self.password,
			'race': self.race,
			'attribute': self.attribute,
			'level': self.level,
			'atk': self.atk,
			'defend': self.defend,
			'desc': self.desc,
			'img': self.img
		}
		return data

class card_bag(db.Model):
	"""卡包"""
	__tablename__ = "yxw_card_bag"

	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.ForeignKey("yxw_user.id"), nullable=True) # 用户id


class middle(db.Model):
	"""中间表"""
	__tablename__ = "yxw_middle"

	id = db.Column(db.Integer, primary_key=True)
	cards_id = db.Column(db.ForeignKey("yxw_cards.id"), nullable=True) # 卡牌id
	card_bag_id = db.Column(db.ForeignKey("yxw_card_bag.id"), nullable=True) # 卡包id
