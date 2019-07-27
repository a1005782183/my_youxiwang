from youxiwang import db, app

from youxiwang.models import cards

c = cards(name='whoareyou',card_type='怪兽|效果|同盟', password=47228077, race='机械',attribute='光',level=4, atk=500, defend=400,desc=' 1回合1次，自己的主要阶段时可以当作装备卡使用给自己场上的名字带有', img='47228077.jpg')
c.commit()

for a in cards.query.whoosh_search(u'wh').all():
	print(a)