# -*- coding:GBK -*-

import iworld2d
import iworld3d
import game
import iphy3d
import math

import tower_init
import tower_const
import tower_player
import tower_obj

TIPS = """
极光工作室：摩天大楼demo
空格键-----房屋下落
ESC-----刷新重来
"""

bgs = None

API = None

towers = []

col_draw = False

cam_rot = 0

CAMERA_MOVE_STEP = 1

def init(api):
	API = api

	global text
	text = API.get_text_panel()
	text.set_text(TIPS)
	text.set_coord((30, 50))

	iworld2d.init(4)

	global bgs
	bgs = []
	bgs.append(iworld2d.image2d("tower/res/bg/bg_far.png", layer_id=0))
	bgs.append(iworld2d.image2d("tower/res/bg/bg_mid.png", layer_id=1))
	bgs.append(iworld2d.image2d("tower/res/bg/bg_near.png", layer_id=3))
	bgs[1].pos = (0, 260)
	bgs[2].pos = (0, 580)

	iworld3d.init()
	iworld3d.add_scene_to_layer2d(tower_const.SCENE_LAYER)

	create_objs()

def create_tower():
	t = tower_player.CTower()
	t.create_sprite("tower/res/world3d/tower0.gim", "tower0", tower_const.SCENE_LAYER)
	t.create_phy(tower_const.SCENE_LAYER)
	#t.pos = tower_player.g_tower_init_pos
	#t.set_sprite_key(0, -10, 0)
	#t.sprite.rotate_to_xyz(y=math.pi)
	return t

def create_objs():
	stone = tower_obj.CGameObj()
	stone.create_sprite("tower/res/world3d/platform.gim", "platform", tower_const.SCENE_LAYER)
	stone.create_phy(tower_const.SCENE_LAYER)
	stone.sprite.scale = (0.1, 0.1, 0.1)
	stone.pos = (-10, 40, -100)
	iphy3d.update(tower_const.SCENE_LAYER)

def on_key_msg(msg, key_code):
	global towers
	if msg == game.MSG_KEY_UP:
		if key_code ==  game.VK_SPACE:
			t = create_tower()
			#t.pos = tower_const.TOWER_INIT_POS
			towers.append(t)
			iphy3d.update(tower_const.SCENE_LAYER)

		elif key_code == game.VK_ESCAPE:
			for t in towers:
				t.destroy()
			towers = []
			iphy3d.update(tower_const.SCENE_LAYER)

		elif key_code == game.VK_F3:
			global col_draw
			col_draw = not col_draw
			print col_draw
			iphy3d.set_debug_draw(tower_const.SCENE_LAYER, col_draw)
			iphy3d.update(tower_const.SCENE_LAYER)

	if msg == game.MSG_KEY_PRESSED:
		key = key_code
		global cam_rot
		if key >= game.VK_A and key <= game.VK_Z:
			# 相机控制演示
			# 小键盘46表示相机沿x轴左右平移
			# 小键盘28表示相机沿y轴上下平移
			# 小键盘13表示相机沿z轴前后平移
			# 小键盘79表示相机沿y轴左右旋转
			# 小键盘5表示相机对准主角小蛋黄
			# 小键盘0表示相机恢复初始状态
			cam = iworld3d.get_camera(tower_const.SCENE_LAYER)
			position = cam.position
			if key == game.VK_Q:
				position.x -= CAMERA_MOVE_STEP
			elif key == game.VK_W:
				position.x += CAMERA_MOVE_STEP
			elif key == game.VK_E:
				position.y -= CAMERA_MOVE_STEP
			elif key == game.VK_R:
				position.y += CAMERA_MOVE_STEP
			elif key == game.VK_A:
				position.z += CAMERA_MOVE_STEP
			elif key == game.VK_S:
				position.z -= CAMERA_MOVE_STEP
			elif key == game.VK_D:
				cam_rot -= 1
				cam.rotate_to_xyz(y=cam_rot*math.pi/200)
			elif key == game.VK_F:
				cam_rot += 1
				cam.rotate_to_xyz(y=cam_rot*math.pi/200)
			elif key == game.VK_Z:
				cam.look_at(player.sprite.position)
			elif key == game.VK_X:
				# 还原位置
				position = math3d.vector(0,0,0)
				forward = math3d.vector(0,0,-1)
				up = math3d.vector(0,-1,0)
				# 还原旋转矩阵
				# 演示rotation_matrix的用法
				cam.rotation_matrix = math3d.matrix.make_orient(forward, up)
				# 实际上此用法等同于这个接口
				#iworld3d.set_camera_placement(tower_const.SCENE_LAYER, position, forward, up)
			cam.position = position

def render():
	pass

def logic():
	for t in towers:
		t.update()

def post_logic():
	pass

def on_mouse_msg (msg, key):
	pass

def on_mouse_wheel (msg, delta, key_state):
	pass
