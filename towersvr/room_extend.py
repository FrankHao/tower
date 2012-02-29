# -*- coding:GBK -*-

import hall_callback
import sdk_version
## ���ô˺���ʹ��iTownSDK�ṩ����Ϸ��������
## ����version��ָʹ�õ�sdk�������˵İ汾��
## Ŀǰֻ��SDK_VERSION_1_0����ʾiTownSDK�ӿڵ�1.0�汾��
hall_callback.use_hall(version=sdk_version.SDK_VERSION_1_0)



## g_roomģ�飬����Ϸ�������ʵ��
import g_room
## ��Ϣ�Ķ���
import g_msg


def get_callback():
	event_callback = {
		## 'msg': callback_function,
	}
	return event_callback
	
def init():
	global event_callback

	### ������Ϸ����� ��Ϣ���� �� ��Ϣ�ص�����
	hall_callback.register_game_room_msgdefine_and_callback(\
		g_msg.msg, get_callback())

	### ���÷�����Ķ���
	hall_callback.set_class_define(
		{ 
			1:(             ## ��Ϸģʽ
				1,          ## ����Ϸģʽ����С����
				1,           ## ����Ϸģʽ���������
				g_room.Room, ## ����Ϸģʽ���ڵķ����߼���
				"1�˲���ģʽ", ## ����Ϸģʽ���������ڿͻ��˴������䣬��ԵȽ������ʾ
				0,          ## ��ģʽ�Ƿ�����ģʽ��������Բ鿴�ĵ��й��ڡ����ط��䡱�Ĳ���
			)
		} 
	)

### ���ó�ʼ������
hall_callback.init = init

