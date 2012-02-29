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
	t.create_sprite("tower/res/world3d/xiaodanhuang.gim", "xdh", tower_const.SCENE_LAYER)
	t.create_phy(tower_const.SCENE_LAYER)
	t.set_sprite_key(0, 15, 0)
	t.sprite.rotate_to_xyz(y=math.pi)
	return t

def create_objs():
	stone = tower_obj.CGameObj()
	stone.create_sprite("tower/res/world3d/dalumian.gim", "s1", tower_const.SCENE_LAYER)
	stone.create_phy(tower_const.SCENE_LAYER)
	stone.sprite.scale = (0.1, 0.1, 0.1)
	stone.pos = (-10, 30, -100)
	iphy3d.update(tower_const.SCENE_LAYER)

def on_key_msg(msg, key_code):
	global towers
	if msg == game.MSG_KEY_UP:
		if key_code ==  game.VK_SPACE:
			t = create_tower()
			t.pos = tower_const.TOWER_INIT_POS
			towers.append(t)
			iphy3d.update(tower_const.SCENE_LAYER)

		elif key_code == game.VK_ESCAPE:
			for t in towers:
				t.destroy()	
			towers = []
			iphy3d.update(tower_const.SCENE_LAYER)

		elif key == game.VK_F2:
			global col_draw 
			col_draw = not col_draw 
			iphy3d.set_debug_draw(eggyolk2_const.SCENE_LAYER, col_draw)

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
