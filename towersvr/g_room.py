#-*- coding:GBK -*-

import hall_object
import hall_callback

class Room(hall_object.HallRoom):
	def __init__(self, room_id=0, name='', mode=0, host=0, pwd='', max_num=0):

		super(Room, self).__init__(room_id,
				name, mode, host, pwd, max_num)

		self.msgmgr = hall_callback.get_game_room_msgmgr()
