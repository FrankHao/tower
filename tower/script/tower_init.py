# -*- coding:GBK -*-
# �����ͻ��˳���Ľṹ

import iapi
import g_msg

import tower_world

API = None
_event_map = {}

def init (**args):
	# ����args���ֵ�,����:
		# {'uid': '20001', 'gamemode': '1', 'gameid': '99',
		# 'urs': 'user', 'roomid': '0'}
	# ����uid�ǽ�ɫ��Ψһid
	# urs�Ǳ��ε�½���ʺţ�����Ϊ�գ�������ʹ��
	# gamemode����Ϸģʽ
	# gameid����Ϸ���
	# roomid�Ƿ�����

	# ��ʼ��API: API = iapi.API()
	# ��ʱ�����ʹ��iapi�ṩ�ĺ����ˡ�
	# ��Ҫע����ǣ�iapi�������汾�ģ���������Ĭ�Ͼ���ʹ�����°汾��API��
	# �����̻�ĳ���汾API������1.0�����������
	# API = iapi. API_1_0 ()
	global API
	API = iapi.API()

	# ע��ص�, ����˵����鿴API�ĵ�
	API.register_callback( int(args['gameid']),
		my_logic, my_render, my_post_logic,
		on_key_msg = on_key_msg,
		on_mouse_msg = on_mouse_msg,
		on_mouse_wheel =  on_mouse_wheel)

	# ��ʼ������
	API.register_game_room_msgdefine_and_callback(g_msg.msg, get_event_map())

	tower_world.init(API)

def get_event_map():
	global _event_map
	# if not _event_map:
		# _event_map['msg'] = callback_function
	return _event_map

def force_destroy():
	pass

# �ص�����
def my_logic ():
	tower_world.logic()


def my_post_logic ():
	tower_world.post_logic()

def my_render ():
	tower_world.render()

def on_key_msg (msg, key_code):
	# �����¼��ص�
	tower_world.on_key_msg(msg, key_code)


def on_mouse_msg (msg, key):
	# ����¼��ص�
	tower_world.on_mouse_msg(msg, key)


def on_mouse_wheel (msg, delta, key_state):
	# �������¼��ص�
	tower_world.on_mouse_wheel(msg, delta, key_state)

