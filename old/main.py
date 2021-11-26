import pygame
from math import floor
from screens import Loading_Screen,Game_screen,Infos_screen
from engine import Player,Enemy,Projectile
from random import uniform,choice
import sys

def main():
	resolution=(1024,768)
	pygame.init()
	pygame.display.set_caption("insert_your_soul")
	screen_window=pygame.display.set_mode(resolution,depth=16)
	clock=pygame.time.Clock()
	launch=Loading_Screen.loading_png()
	game_elements=Game_screen.loading_png()
	infos_bg=Infos_screen.loading_png()
	
	track_time=0

	screen_window.blit(launch["bg"],[0,0])
	screen_window.blit(launch["SOUL_1"],[405,470])
	screen_window.blit(launch["INFOS_1"],[20,672])
	pygame.display.update()
	
	index_soul=0
	index_loading=1
	index_game=0
	index_infos=0
	shootloop_priest=0
	shootloop_demon=0
	
	player_right=[game_elements["perso_1"],game_elements["perso_2"],game_elements["perso_3"]]
	player_left=[game_elements["perso_1_left"],game_elements["perso_2_left"],game_elements["perso_3_left"]]
	enemy=[game_elements["demon_1"],game_elements["demon_2"],game_elements["demon_3"]]

	priest_init=game_elements["perso_2"]
	last_key=None
	k_pressed=None
	priest=Player(1024/2-floor(59/2),481-143,59,143,player_right,player_left,priest_init,last_key)
	
	x_spawn_demon=floor(choice([10,937]))
	dir=floor(choice([0,1]))
	demon=Enemy(x_spawn_demon,481-143,77,144,0,1024,enemy,dir)
	proj_priest_alive=0

	
	launched=True
	while launched:
		for event in pygame.event.get():
			if event.type==pygame.KEYDOWN:
				if pygame.key.get_pressed()[pygame.K_ESCAPE]:
					launched=False
			if event.type==pygame.QUIT:
				launched=False
			if event.type==pygame.MOUSEBUTTONDOWN:
				status_launch_game=Loading_Screen.click_button(405,630,470,663)
				if status_launch_game==True:
					index_game=1
					index_loading=0
					track_time=0
					track_time2=0
					track_time3=0
					track_time4=0
					wait_spawn=0
					status_priest=0
					vie=5
					init_score=1
					score=0
					score_prev="0"
					vie_prev="5"
				status_launch_infos=Loading_Screen.click_button(20,296,672,756)
				if status_launch_infos==True:
					index_infos=1
					index_loading=0
					track_time=0
					
					
### ecran de chargement###
		if index_loading==1:
	#clignotement boutton executable

			values_blink_soul=Loading_Screen.blink_soul_butt(track_time=track_time,clock=clock,index_soul=index_soul,soul_butt_1=launch["SOUL_1"],soul_butt_2=launch["SOUL_2"])
			screen_window.blit(values_blink_soul[0],[405,470])
			index_soul=values_blink_soul[1]
			track_time=values_blink_soul[2]

	#positionnnement souris dans ecran
			highlight_soul=Loading_Screen.highlight_butt(405,630,470,663,butt_state_1=launch["SOUL_1"],butt_state_2=launch["SOUL_2"])
			if highlight_soul==launch["SOUL_2"]:
				screen_window.blit(highlight_soul,[405,470])
			highlight_infos=Loading_Screen.highlight_butt(20,296,672,756,butt_state_1=launch["INFOS_1"],butt_state_2=launch["INFOS_2"])
			screen_window.blit(highlight_infos,[20,672])

###ecran de jeu###


		if index_game==1:
			screen_window.blit(game_elements["game_screen_1"],[0,0])
			if init_score==1:
				screen_window.blit(game_elements["5_vert"],[598,677])
				screen_window.blit(game_elements["0_rouge"],[845,677])
				screen_window.blit(game_elements["0_rouge"],[889,677])
				init_score=0

#gestion du pretre


			keys = pygame.key.get_pressed()
			if keys[pygame.K_SPACE] and shootloop_priest==0:
				shootloop_priest=1
				
				if priest.left and priest.isJump==False:
					facing=-1
					proj_priest_alive=1
					proj_priest=Projectile(priest.x,priest.y+floor(priest.height/2),35,demon.hitbox,game_elements["missile_sacre_left"],facing,'demon')


				elif priest.right and priest.isJump==False:
					facing=1
					proj_priest_alive=1
					proj_priest=Projectile(priest.x+priest.width,priest.y+floor(priest.height/2),35,demon.hitbox,game_elements["missile_sacre"],facing,'demon')

			
			if keys[pygame.K_q] and priest.x>priest.vel:
				k_pressed='left'
				priest.x-=priest.vel
				priest.left=True
				priest.right=False
				priest.standing=False
			elif keys[pygame.K_d] and priest.x<1024-priest.width-priest.vel:
				k_pressed='right'
				priest.x+=priest.vel
				priest.left=False
				priest.right=True
				priest.standing=False
			else:
				priest.standing=True
				priest.walkCount = 0
			
			if not(priest.isJump):
				if keys[pygame.K_z]:
					k_pressed='jump'
					priest.isJump=True
					priest.right=False
					priest.left=False
					priest.standing=False
					priest.walkCount=0
			if priest.isJump:
				if priest.jumpCount >=-10:
					neg=1
					if priest.jumpCount<0:
						neg=-1
					priest.y-=(priest.jumpCount**2)*0.5*neg
					priest.jumpCount-=1
				else:
					priest.isJump=False
					priest.standing=True
					priest.jumpCount=10

#gestion collision pretre avec demon+affichage pretre

			if priest.hitbox[0]>demon.hitbox[0] and priest.hitbox[0]<demon.hitbox[0]+demon.hitbox[2] or priest.hitbox[0]+priest.hitbox[2]>demon.hitbox[0] and priest.hitbox[0]+priest.hitbox[2]<demon.hitbox[0]+demon.hitbox[2]:
				track_time4=track_time4+clock.get_time()
				vie-=1
				vie_prev=str(vie)
				if vie==-1:
					vie_prev="0"
					sys.exit()
				
				if track_time4>500:
					x_spawn_priest=floor(uniform(10,937))
					priest=Player(x_spawn_priest,481-143,59,143,player_right,player_left,priest_init,last_key)
					wait_spawn=0
				else:
					wait_spawn=1
			else:
				if wait_spawn==0:
					priest_update=priest.draw(track_time,clock)
					priest.hitbox=(priest.x,priest.y,59,143)
					priest.old_frame=priest_update[0]
					track_time=priest_update[1]
					priest.last_key=k_pressed
					screen_window.blit(priest_update[0],[priest.x,priest.y])
			screen_window.blit(game_elements[vie_prev+"_vert"],[598,677])

#gestion tir sur demon et affichage demon
			if proj_priest_alive==1:
				proj_priest.hitbox=demon.hitbox
				proj_priest_update=proj_priest.gestion()
				if proj_priest_update[0]==None:
					proj_priest_alive=0
					shootloop_priest=0
					status_demon=proj_priest_update[1]
					if wait_spawn==1:
						status_demon=1
				else:
					screen_window.blit(proj_priest_update[0],[proj_priest.x,proj_priest.y])
					if wait_spawn==1:
						status_demon=1
					else:
						status_demon=0
			else:
				if wait_spawn==1:
					status_demon=1
				else:
					status_demon=0
					
					
					
#affichage
			
			
			if status_demon==0:
				demon_update=demon.draw(track_time2,clock)
				track_time2=demon_update[1]
				demon.hitbox=(demon.x,demon.y,77,144)
				screen_window.blit(demon_update[0],[demon.x,demon.y])
				
			else:
				
				track_time3=track_time3+clock.get_time()
				if track_time3 > 500:
					x_spawn_demon=floor(uniform(10,937))
					dir=floor(choice([0,1]))
					demon=Enemy(x_spawn_demon,481-143,77,144,0,1024,enemy,dir)
					scoring=proj_priest.hit(score)
					score=scoring[0]
					score_prev=scoring[1]
					print(score_prev)
					wait_spawn=0
				else:
					wait_spawn=1
					
			
			
			if len(score_prev)>1:
				screen_window.blit(game_elements[score_prev[0]+"_rouge"],[845,677])
				screen_window.blit(game_elements[score_prev[1]+"_rouge"],[889,677])
			else:
				screen_window.blit(game_elements["0_rouge"],[845,677])
				screen_window.blit(game_elements[score_prev[0]+"_rouge"],[889,677])

###page infos###
		if index_infos==1:
			
			screen_window.blit(infos_bg["infos_screen"],[0,0])
		pygame.display.update()
		clock.tick(60)







if __name__=="__main__":
	main()