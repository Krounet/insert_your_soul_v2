import pygame
from math import floor
		

class Player(object):
	def __init__(self,x,y,width,height,player_elements_right,player_elements_left,old_frame,last_key):
		self.x=x
		self.y=y
		self.width=width
		self.height=height
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
		
	
	def draw(self,track_time,clock):
		

		track_time=track_time+clock.get_time() 
		
		if track_time>100:
			
		
			if self.walkCount+1>=3 and self.left:
				self.walkCount=0
				self.player_elements_left[2]
			if self.walkCount+1>=3 and self.right:
				self.walkCount=0
				self.player_elements_right[2]
			if not(self.standing):
				if self.left:
					frame=self.player_elements_left[self.walkCount]
					self.walkCount+=1
				if self.right:
					frame=self.player_elements_right[self.walkCount]
					self.walkCount+=1
				if self.isJump:
					frame=self.old_frame
			track_time=0
		else:
			if not(self.standing):
				if self.left:
					frame=self.player_elements_left[self.walkCount]
					
				if self.right:
					frame=self.player_elements_right[self.walkCount]
					
				if self.isJump:
					frame=self.old_frame
			
			


		if self.standing:
			
			if self.last_key=='left':
				frame=self.player_elements_left[1]
			if self.last_key=='right':
				frame=self.player_elements_right[1]
			if self.last_key=='jump':
				frame=self.old_frame
			if self.last_key==None:
				frame=self.player_elements_right[1]
		return frame,track_time

class Enemy(object):
	def __init__(self,x,y,width,height,origin,end,enemy_elements,dir):
		self.x=x
		self.y=y
		self.width=width
		self.height=height
		self.end=end
		self.origin=origin
		self.dir=dir
		self.enemy_elements=enemy_elements
		self.path=[self.origin,self.end]
		self.walkCount=0
		self.vel=2
		self.hitbox=(self.x,self.y,width,height)
	
	
		
	def draw(self,track_time,clock):
		track_time=track_time+clock.get_time() 
		self.move()
		if track_time>100:
		
			if self.walkCount+1>=3:
				self.walkCount=0
				frame=self.enemy_elements[2]
			
			else:
					frame=self.enemy_elements[self.walkCount]
					self.walkCount+=1
					
			self.hitbox=(self.x,self.y,self.width,self.height)
			track_time=0
		else:
			frame=self.enemy_elements[self.walkCount]
			
		return frame,track_time

	def move(self):
		if self.dir==1:
			self.vel=self.vel*-1
			self.dir=0
		if self.vel>0:
			if self.x+self.width+self.vel<=self.path[1]:
				self.x+=self.vel
			else:
				self.walkCount=0
				self.vel=self.vel*-1
				self.x+=self.vel
				
		else:
			if self.x-self.vel>=self.path[0]:
				self.x+=self.vel
			else:
				self.walkCount=0
				self.vel=self.vel*-1
				self.x+=self.vel
				
		
class Projectile(object):
	def __init__(self,x,y,width,hitbox,proj_sprite,facing,victim):
		self.x=x
		self.y=y
		self.proj_sprite=proj_sprite
		self.facing=facing
		self.vel=3*facing
		self.hitbox=hitbox
		self.width=width
		self.victim=victim
	
	def gestion(self):
		touche=0
		if self.facing==1:
			if self.y<self.hitbox[1]+self.hitbox[3] and self.y>self.hitbox[1]:
				if self.x+self.width>self.hitbox[0] and self.x+self.width<self.hitbox[0]+self.hitbox[2]:
					
					touche=1
					frame=None
			if self.x<1024 and touche==0:
				self.x+=self.vel
				frame=self.proj_sprite
			if self.x>=1024 and touche==0:
				frame=None
		
		if self.facing==-1:
			if self.y<self.hitbox[1]+self.hitbox[3] and self.y>self.hitbox[1]:
				if self.x>self.hitbox[0] and self.x<self.hitbox[0]+self.hitbox[2]:
					touche=1
					frame=None
			if self.x>0 and touche==0:
				self.x+=self.vel
				frame=self.proj_sprite
			if self.x<=0 and touche==0:
				frame=None
		return frame,touche
			
	def hit(self,score):
		score+=1
		conv_string=str(score)

		return score,conv_string
	

