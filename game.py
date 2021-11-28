import pygame
from loading_sprite import Loading_sprite
from player import Player
class Game:

	def __init__(self):
		# Démarrage
		self.running = True
		self.clock=0

		# Affichage de la fenêtre
		self.screen = pygame.display.set_mode((1024,768))
		pygame.display.set_caption("insert your soul")
		
		#chargement elements graphiques
		self.launch_elements = Loading_sprite.launch_screen()
		self.game_elements=Loading_sprite.game_screen()
		self.infos_elements=Loading_sprite.infos_screen()
		

		
	def blink_launch_butt(self,track_time,index_launch,launch_butt_1,launch_butt_2):
		#clignotement boutton de lancement. si track_time > 500 ms changement d'état
		track_time=track_time+self.clock.get_time() 
		if track_time<=500 and index_launch==0:
			butt_version=launch_butt_1
		
		if track_time<=500 and index_launch==1:
			butt_version=launch_butt_2
		
			
		if track_time >= 500:
			if index_launch==0:
				butt_version=launch_butt_2
				index_launch=1
				track_time=0
			else :
				butt_version=launch_butt_1
				index_launch=0
				track_time=0
		return butt_version,index_launch,track_time
	
	def highlight_butt(self,xmin,xmax,ymin,ymax,highlight_state_1,highlight_state_2):
		#Highlight boutons de lancement ou infos
		if pygame.mouse.get_pos()[0]>xmin and pygame.mouse.get_pos()[0]<xmax and pygame.mouse.get_pos()[1]>ymin and pygame.mouse.get_pos()[1]<ymax:
			image_state=highlight_state_2
		else:
			image_state=highlight_state_1
		return image_state
	
	
	def click_button(self,xmin,xmax,ymin,ymax):
		#action lors d'un click
		if pygame.mouse.get_pos()[0]>xmin and pygame.mouse.get_pos()[0]<xmax and pygame.mouse.get_pos()[1]>ymin and pygame.mouse.get_pos()[1]<ymax:
			change = True
		else:
			change = False
		return change
	
	def handler_input(self):
		pressed=pygame.key.get_pressed()
		#Escape pour quitter le jeu
		if pressed[pygame.K_ESCAPE]:
			self.running=False
		#Z ou Up pour sauter (fonction à créer dans player)
		elif pressed[pygame.K_z] or pressed[pygame.K_UP]:
			self.player.move_player("jump")
		#Q ou left pour aller à gauche (fonction à créer dans player)
		elif pressed[pygame.K_q] or pressed[pygame.K_LEFT]:
			self.player.move_player("left")
		#D ou right pour aller à droite (fonction à créer dans player)
		elif pressed[pygame.K_d] or pressed[pygame.K_RIGHT]:
			self.player.move_player("right")
		#Espace pour tirer (fcontion à créer)
		elif pressed[pygame.K_SPACE]:
			self.player.shoot()

		
	
	
	def run(self):
		self.clock=pygame.time.Clock()
		track_time=0
		index_launch=0
		index_game=0
		index_infos=0
		index_blink=0
		while self.running:
			#self.player.save_location()
			self.handler_input()
			#self.update()
			#pygame.display.flip()

			#gestion event commande
			for event in pygame.event.get():
						
				if event.type==pygame.QUIT:
					self.running = False
					
				if event.type==pygame.MOUSEBUTTONDOWN:
					status_launch_game=self.click_button(405,630,470,663)
					status_launch_infos=self.click_button(20,296,672,756)
					if status_launch_game==True:
						index_game=1
						
					elif status_launch_infos==True:
						index_infos=1
						
			if index_game==1:
				return 0
				#gestion ecran de jeu
			elif index_infos==1:
				#lancement ecran d'infon
				self.screen.blit(self.infos_elements["infos_screen"],[0,0])
				
				#Penser à ajouter un bouton pour retour à l'accueil
				
			else:
				#gestion écran de chargement
				self.screen.blit(self.launch_elements["bg"],[0,0])
				values_blink_butt=self.blink_launch_butt(track_time=track_time,index_launch=index_blink,launch_butt_1=self.launch_elements["SOUL_1"],launch_butt_2=self.launch_elements["SOUL_2"])
				self.screen.blit(values_blink_butt[0],[405,470])
				index_blink=values_blink_butt[1]
				track_time=values_blink_butt[2]
				
				#highlight infos buttons + launch buttons
				highlight_launch=self.highlight_butt(405,630,470,663,highlight_state_1=self.launch_elements["SOUL_1"],highlight_state_2=self.launch_elements["SOUL_2"])
				if highlight_launch==self.launch_elements["SOUL_2"]:
					self.screen.blit(highlight_launch,[405,470])
				highlight_infos=self.highlight_butt(20,296,672,756,highlight_state_1=self.launch_elements["INFOS_1"],highlight_state_2=self.launch_elements["INFOS_2"])
				self.screen.blit(highlight_infos,[20,672])
				
			pygame.display.update()
			self.clock.tick(60)
		pygame.quit()