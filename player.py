import pygame

class Player(object):

		def __init__(self,x,y,width,height,player_elements_right,player_elements_left):
		self.x=x
		self.y=y
		self.player_elements_right=player_elements_right
		self.player_elements_left=player_elements_left
		self.vel=5
		self.isJump=False
		self.left=False
		self.right=False
		self.walkCount=0
		self.jumpCount=10
		self.standing=True
		self.hitbox=(self.x,self.y,self.width,self.height)
		self.old_frame=old_frame
		self.last_key=last_key