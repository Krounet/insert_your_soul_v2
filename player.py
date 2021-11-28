import pygame

class Player(object):

	def __init__(self,x,y,width,height,player_elements_right,player_elements_left):
		self.x=x
		self.y=y
		self.width=width
		self.height=height
		self.hitbox=(self.x,self.y,self.width,self.height)
		self.player_elements_right=player_elements_right
		self.player_elements_left=player_elements_left
		self.vel=5
		self.isJump=False
		self.left=False
		self.right=False
		self.walkCount=0
		self.jumpCount=10
		self.standing=True


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



class Projectile(object):

	def __init__(self,x,y,width,hitbox_ennemy,proj_sprite,facing,victim):
		self.x=x
		self.y=y
		self.proj_sprite=proj_sprite
		self.facing=facing
		self.vel=10*facing
		self.hitbox=hitbox_ennemy
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