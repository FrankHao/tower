# -*- coding:GBK -*-

import hall_callback
import sdk_version
## 调用此函数使用iTownSDK提供的游戏公共大厅
## 参数version是指使用的sdk服务器端的版本。
## 目前只有SDK_VERSION_1_0，表示iTownSDK接口的1.0版本。
hall_callback.use_hall(version=sdk_version.SDK_VERSION_1_0)



## g_room模块，是游戏房间类的实现
import g_room
## 消息的定义
import g_msg


def get_callback():
	event_callback = {
		## 'msg': callback_function,
	}
	return event_callback
	
def init():
	global event_callback

	### 设置游戏房间的 消息定义 和 消息回调函数
	hall_callback.register_game_room_msgdefine_and_callback(\
		g_msg.msg, get_callback())

	### 设置房间类的定义
	hall_callback.set_class_define(
		{ 
			1:(             ## 游戏模式
				1,          ## 此游戏模式的最小人数
				1,           ## 此游戏模式的最大人数
				g_room.Room, ## 此游戏模式对于的房间逻辑类
				"1人测试模式", ## 此游戏模式的命名，在客户端创建房间，配对等界面会显示
				0,          ## 此模式是否隐藏模式，具体可以查看文档中关于“隐藏房间”的部分
			)
		} 
	)

### 设置初始化函数
hall_callback.init = init

