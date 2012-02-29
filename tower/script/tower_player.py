# -*- coding:GBK -*-

import iphy3d
import math3d

import tower_obj
import tower_const


class CTower(tower_obj.CGameObj):
	def init(self):
		self.bill = None
		self.moving_dir = math3d.vector(0, 0, 0)
		self.target_pos = math3d.vector(0, 0, 0)

	def create_sprite(self, gim_file, name, layer_id):
		super(CTower, self).create_sprite(gim_file, name, layer_id)
		self.animations = ['npc_act_001', 'npc_act_003']

		self.set_state(tower_const.TOWER_STATE_DROPPING)

	def create_bill(self, swf_file, text=""):
		if self.bill:
			self.bill.destroy()
		self.bill = iworld3d.space_movie(swf_file, True, pixel_unit=0.1, layer_id=eggyolk2_const.SCENE_LAYER)
		self.sprite.bind("cstop", self.bill)
		self.bill.billboard_type = True

		if text:
			self.bill.movie.set_variable("name.text", text)

	def destroy_bill(self):
		if self.bill:
			self.bill.destroy()
			self.bill = None

	def create_phy(self, layer_id):
		self.phy = iphy3d.col_sphere(tower_const.RADIUS, tower_const.COL_NPC, tower_const.COL_NPC)
		self.phy.add_to_layer(layer_id)

	def set_state(self, state):
		self.state = state
		self.sprite.play_animation(self.animations[self.state])

	def sweep_test(self, start, end):
		ext_end = start + (end - start) * 2.0
		sweep_filter = iphy3d.col_filter(0, 0, iphy3d.EXCLUDE_FILTER)
		#sweep_filter = iphy3d.col_filter(tower_const.COL_ROAD | tower_const.COL_NPC, 0, iphy3d.EXCLUDE_FILTER) 
		#sweep_filter = iphy3d.col_filter(tower_const.COL_NPC , tower_const.COL_NPC, iphy3d.EQUAL_FILTER)
		#sweep_filter = iphy3d.col_filter(tower_const.COL_NPC, tower_const.COL_ROAD, iphy3d.EQUAL_FILTER) 
		#sweep_filter = iphy3d.col_filter(tower_const.COL_NPC , tower_const.COL_ROAD, iphy3d.INEQUAL_FILTER)
		try:
			result = iphy3d.sweep_test(tower_const.SCENE_LAYER, self.phy, start, ext_end, sweep_filter)
		except iphy3d.iphy3d_exception, e:
			print e
			return iphy3d.col_result()
		if result.hit:
			if result.fraction > 0.5 + tower_const.FLOAT_EPSILON:
				return iphy3d.col_result()
			else:
				result.fraction *= 2.0
				return result
		return result


	def update_dropping(self):
		if self.state == tower_const.TOWER_STATE_MOVING:
			return

		down = math3d.vector(0, tower_const.GRAVITY, 0)

		cur_pos = math3d.vector(*self.pos)

		self.target_pos = cur_pos + down

		result = self.sweep_test(cur_pos, self.target_pos)

		if not result.hit:
			self.pos = self.target_pos.x, self.target_pos.y, self.target_pos.z
			self.set_state(tower_const.TOWER_STATE_DROPPING)
			return
		self.update_collide_pos(result.fraction)
		self.set_state(tower_const.TOWER_STATE_MOVING)

	def update_collide_pos(self, fraction):
		cur_pos = math3d.vector(*self.pos)
		length = (cur_pos - self.target_pos).length
		moved = length * fraction
		if moved < tower_const.MARGIN:
			return

		#TODO: intrp ?
		cur_pos.intrp(cur_pos, self.target_pos, (moved - tower_const.MARGIN) / length)
		self.pos = cur_pos.x, cur_pos.y, cur_pos.z

	def update_moving(self):
		if self.state == tower_const.TOWER_STATE_DROPPING:
			return
		self.moving()

	def moving(self):

		#TODO math3d.vector api ?
		if self.moving_dir.is_zero:
			return
		cur_pos = math3d.vector(*self.pos)
		self.target_pos = cur_pos + self.moving_dir
		result = self.sweep_test(cur_pos, self.target_pos)

		#TODO hit ?
		if not result.hit:
			self.pos = self.target_pos.x, self.target_pos.y, self.target_pos.z
			return
		self.update_collide_pos(result.fraction)
	

	def update(self):
		self.update_dropping()
		self.update_moving()

	def switch_phy_type(self, col_type, layer_id):
		if self.phy is	None:
			return
		self.set_phy_key(0, 0, 0)
		if col_type == tower_const.COL_TYPE_CAPSULE:
			temp = iphy3d.col_capsule(4, 4, tower_const.COL_NPC, eggyolk2_const.COL_NPC)
		elif col_type == tower_const.COL_TYPE_CYLINDER:
			temp = iphy3d.col_cylinder(4, 6, tower_const.COL_NPC, eggyolk2_const.COL_NPC)
		elif col_type == tower_const.COL_TYPE_MODEL:
			temp = iphy3d.col_model(self.sprite, tower_const.COL_NPC, eggyolk2_const.COL_NPC)
			temp.rotation_matrix = self.sprite.rotation_matrix 
			self.set_phy_key(0, 7, 0) 
		elif col_type == tower_const.COL_TYPE_SPHERE:
			temp = iphy3d.col_sphere(6, tower_const.COL_NPC, eggyolk2_const.COL_NPC)
		else:
			return
		self.phy.remove_from_layer()
		self.phy = temp
		self.pos = self.pos
		self.phy.add_to_layer(layer_id)
		iphy3d.update(layer_id)
