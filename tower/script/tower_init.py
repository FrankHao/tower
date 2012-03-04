# -*- coding:GBK -*-
# 创建客户端程序的结构

import iapi
import g_msg

import tower_world

API = None
_event_map = {}

def init (**args):
	# 参数args是字典,如下:
		# {'uid': '20001', 'gamemode': '1', 'gameid': '99',
		# 'urs': 'user', 'roomid': '0'}
	# 其中uid是角色的唯一id
	# urs是本次登陆的帐号，可能为空，不建议使用
	# gamemode是游戏模式
	# gameid是游戏编号
	# roomid是房间编号

	# 初始化API: API = iapi.API()
	# 此时便可以使用iapi提供的函数了。
	# 需要注意的是，iapi会升级版本的，这样生成默认就是使用最新版本的API，
	# 如果想固化某个版本API，例如1.0则可以这样：
	# API = iapi. API_1_0 ()
	global API
	API = iapi.API()

	# 注册回调, 参数说明请查看API文档
	API.register_callback( int(args['gameid']),
		my_logic, my_render, my_post_logic,
		on_key_msg = on_key_msg,
		on_mouse_msg = on_mouse_msg,
		on_mouse_wheel =  on_mouse_wheel)

	# 初始化网络
	API.register_game_room_msgdefine_and_callback(g_msg.msg, get_event_map())

	tower_world.init(API)

def get_event_map():
	global _event_map
	# if not _event_map:
		# _event_map['msg'] = callback_function
	return _event_map

def force_destroy():
	pass

# 回调函数
def my_logic ():
	tower_world.logic()


def my_post_logic ():
	tower_world.post_logic()

def my_render ():
	tower_world.render()

def on_key_msg (msg, key_code):
	# 键盘事件回调
	tower_world.on_key_msg(msg, key_code)


def on_mouse_msg (msg, key):
	# 鼠标事件回调
	tower_world.on_mouse_msg(msg, key)


def on_mouse_wheel (msg, delta, key_state):
	# 鼠标滚轮事件回调
	tower_world.on_mouse_wheel(msg, delta, key_state)

