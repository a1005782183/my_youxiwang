from youxiwang import socket_io
import json
from flask import request
from flask_socketio import join_room, leave_room

@socket_io.on("connect_send")
def connect_send(username):
	'''socket连接'''
	join_room(username)
	print("连接成功", username)

	if username == 'admin1':
		print("接收到了",username)
		socket_io.emit(event="init_token", data=json.dumps({"token": 1}), room="admin")
		socket_io.emit(event="wait_join", data=json.dumps({"username": username}), room="admin")

@socket_io.on("wait_join2")
def wait_join2(username):
	'''客户端1发送给客户端2'''
	if username == 'admin':
		print("wait_join2接收到了",username)
		socket_io.emit(event="wait_join", data=json.dumps({"username": username}), room="admin1")

@socket_io.on("swap")
def swap(username):
	'''交换回合'''

	socket_io.emit(event="show_hhz", data=json.dumps({"username": username}))

# @socket_io.on("send_init_token")
# def init_token(username):
# 	'''初始化token'''
# 	if username == 'admin1':
# 		socket_io.emit(event="init_token", data=json.dumps({"token": token}), room="admin")

@socket_io.on("token")
def token(username):
	'''token'''
	token = 1
	if username == 'admin1':
		print("token接收到了", username)
		socket_io.emit(event="rec_token", data=json.dumps({"token":token, "username": username}), room="admin")
	if username == 'admin':
		print("token接收到了", username)
		socket_io.emit(event="rec_token", data=json.dumps({"token":token, "username": username}), room="admin1")

@socket_io.on("card_luoji")
def card_luoji(id, img, username):
	'''卡牌逻辑socket
		处理卡牌的双方位置等逻辑
	'''
	if username == 'admin1':
		print("接收到了",id, username)
		socket_io.emit(event="zh_success", data=json.dumps({"id": id, "img": img}), room="admin")
	if username == 'admin':
		print("接收到了",id, username)
		socket_io.emit(event="zh_success", data=json.dumps({"id": id, "img": img}), room="admin1")

@socket_io.on("gj_card_luoji")
def card_luoji(id, img, username):
	'''攻击卡牌逻辑socket
		处理卡牌的双方位置等逻辑
	'''
	if username == 'admin1':
		print("接收到了",id, username)
		socket_io.emit(event="gj_success", data=json.dumps({"id": id, "img": img}), room="admin")
	if username == 'admin':
		print("接收到了",id, username)
		socket_io.emit(event="gj_success", data=json.dumps({"id": id, "img": img}), room="admin1")

@socket_io.on("zh_card_luoji")
def zh_card_luoji(id, img, atk, defend, username):
	'''召唤卡牌逻辑socket
		处理卡牌的双方位置等逻辑
	'''
	if username == 'admin1':
		print("接收到了",id, username)
		socket_io.emit(event="ad_success", data=json.dumps({"id": id, "img": img, "atk": atk, "defend": defend}), room="admin")
	if username == 'admin':
		print("接收到了",id, username)
		socket_io.emit(event="ad_success", data=json.dumps({"id": id, "img": img, "atk": atk, "defend": defend}), room="admin1")


@socket_io.on("add_your_hand")
def add_your_hand(username):
	'''增加敌方手牌'''
	if username == 'admin1':
		socket_io.emit(event="rv_add_your_hand", room="admin")
	if username == 'admin':
		socket_io.emit(event="rv_add_your_hand", room="admin1")

@socket_io.on("remove_your_hand")
def remove_your_hand(username):
	'''移除敌方手牌'''
	if username == 'admin1':
		socket_io.emit(event="rv_remove_your_hand", room="admin")
	if username == 'admin':
		socket_io.emit(event="rv_remove_your_hand", room="admin1")


@socket_io.on("md_card")
def md_card(id, md_num, md_img, username):
	'''墓地卡片'''
	if username == 'admin1':
		socket_io.emit(event="rv_md_card", data=json.dumps({"id":id, "md_num": md_num, "md_img": md_img}), room="admin")
	if username == 'admin':
		socket_io.emit(event="rv_md_card", data=json.dumps({"id":id, "md_num": md_num, "md_img": md_img}), room="admin1")

@socket_io.on("send_src")
def send_src(id, src, username):
	'''放置卡牌送去墓地保存的图片'''
	if username == 'admin1':
		socket_io.emit(event="recv_src", data=json.dumps({"id": id, "src":src}), room="admin")
	if username == 'admin':
		socket_io.emit(event="recv_src", data=json.dumps({"id": id, "src":src}), room="admin1")


@socket_io.on("card_group")
def card_group(c_group, username):
	'''刷新对面卡组'''
	if username == 'admin1':
		socket_io.emit(event="c_group", data=json.dumps({"c_group": c_group}), room="admin")
	if username == 'admin':
		socket_io.emit(event="c_group", data=json.dumps({"c_group": c_group}), room="admin1")
