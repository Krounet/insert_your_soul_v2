import pygame

class Game:

	def __init__(self):
		# Démarrage
		self.running = True
		self.clock=0

		# Affichage de la fenêtre
		self.screen = pygame.display.set_mode((1024,768))
		pygame.display.set_caption("insert your soul")
	
	
	def launch_screen(self):
		#chargement elements de l'écran d'accueil
		load_elements={"bg":pygame.image.load("sprites\loading_screen\loading_screen.png"),"SOUL_1":pygame.image.load("sprites\loading_screen\SOUL_exec1.png"),
		"SOUL_2":pygame.image.load("sprites\loading_screen\SOUL_exec2.png"),"INFOS_1":pygame.image.load("sprites\loading_screen\INFOS1.png"),"INFOS_2":pygame.image.load("sprites\loading_screen\INFOS2.png")}
		load_elements["bg"].convert()
		load_elements["SOUL_1"].convert()
		load_elements["SOUL_2"].convert()
		load_elements["INFOS_1"].convert()
		load_elements["INFOS_2"].convert()
		return load_elements
	
	def game_screen(self):
		#chargement éléments du jeu
		load_elements={"game_screen_1":pygame.image.load("sprites\game_screen\game_screen1.png").convert(),"demon_1":pygame.image.load("sprites\demon\demon1.png").convert(),
		"demon_2":pygame.image.load("sprites\demon\demon2.png").convert(),"demon_3":pygame.image.load("sprites\demon\demon3.png").convert(),
		"perso_1":pygame.image.load("sprites\perso_principal\perso_marche1.png").convert(),
		"perso_2":pygame.image.load("sprites\perso_principal\perso_marche2.png").convert(),"perso_3":pygame.image.load("sprites\perso_principal\perso_marche3.png").convert(),
		"missile_sacre":pygame.image.load("sprites\perso_principal\missile_sacre.png").convert(),"perso_1_left":pygame.image.load("sprites\perso_principal\perso_marche1_left.png").convert(),
		"perso_2_left":pygame.image.load("sprites\perso_principal\perso_marche2_left.png").convert(),"perso_3_left":pygame.image.load("sprites\perso_principal\perso_marche3_left.png").convert(),
		"missile_sacre_left":pygame.image.load("sprites\perso_principal\missile_sacre_left.png").convert(),"0_vert":pygame.image.load("sprites\chiffres\chiffre_vert1.png").convert(),
		"1_vert":pygame.image.load("sprites\chiffres\chiffre_vert2.png").convert(),"2_vert":pygame.image.load("sprites\chiffres\chiffre_vert3.png").convert(),
		"3_vert":pygame.image.load("sprites\chiffres\chiffre_vert4.png").convert(),"4_vert":pygame.image.load("sprites\chiffres\chiffre_vert5.png").convert(),
		"5_vert":pygame.image.load("sprites\chiffres\chiffre_vert6.png").convert(),
		"0_rouge":pygame.image.load("sprites\chiffres\chiffre_rouge1.png").convert(),
		"1_rouge":pygame.image.load("sprites\chiffres\chiffre_rouge2.png").convert(),
		"2_rouge":pygame.image.load("sprites\chiffres\chiffre_rouge3.png").convert(),"3_rouge":pygame.image.load("sprites\chiffres\chiffre_rouge4.png").convert(),
		"4_rouge":pygame.image.load("sprites\chiffres\chiffre_rouge5.png").convert(),
		"5_rouge":pygame.image.load("sprites\chiffres\chiffre_rouge6.png").convert(),"6_rouge":pygame.image.load("sprites\chiffres\chiffre_rouge7.png").convert(),
		"7_rouge":pygame.image.load("sprites\chiffres\chiffre_rouge8.png").convert(),
		"8_rouge":pygame.image.load("sprites\chiffres\chiffre_rouge9.png").convert(),"9_rouge":pygame.image.load("sprites\chiffres\chiffre_rouge10.png").convert()}
		return load_elements
		
		
	def infos_screen(self):
		#chargement éléments d'infos du jeu
		load_elements={"infos_screen":pygame.image.load("sprites\infos_screen\INFOSscreen.png").convert()}
		return load_elements
		
	def blink_launch_butt(self,track_time=0,index_launch,launch_butt_1,launch_butt_2):
		#clignotement boutton de lancement
		track_time=track_time+self.clock #timer changement d'état si > 500 ms. 
		if track_time<=500 and index_soul==0:
			butt_version=soul_butt_1
		
		if track_time<=500 and index_soul==1:
			butt_version=soul_butt_2
		
			
		if track_time >= 500:
			if index_soul==0:
				butt_version=soul_butt_2
				index_soul=1
				track_time=0
			else :
				butt_version=soul_butt_1
				index_soul=0
				track_time=0
		return butt_version,index_soul,track_time
	
	def highlight_butt(xmin,xmax,ymin,ymax,butt_state_1,butt_state_2):
		#Highlight boutons de lancement ou infos
		if pygame.mouse.get_pos()[0]>xmin and pygame.mouse.get_pos()[0]<xmax and pygame.mouse.get_pos()[1]>ymin and pygame.mouse.get_pos()[1]<ymax:
			image_state=butt_state_2
		else:
			image_state=butt_state_1
		return image_state
	
	
	def click_button(xmin,xmax,ymin,ymax):
		#action lors d'un click
		if pygame.mouse.get_pos()[0]>xmin and pygame.mouse.get_pos()[0]<xmax and pygame.mouse.get_pos()[1]>ymin and pygame.mouse.get_pos()[1]<ymax:
			change = True
		else:
			change = False
		return change
	
	
	def run(self):
		self.clock=pygame.time.Clock
		while self.running:
			self.player.save_location()
			self.handler_input()
			self.update()
			pygame.display.flip()

			#gestion event commande
			for event in pygame.event.get():
				if event.type==pygame.KEYDOWN:
					if pygame.key.get_pressed()[pygame.K_ESCAPE]:
						launched=False
						
				if event.type==pygame.QUIT:
					self.running = False
					
				if event.type==pygame.MOUSEBUTTONDOWN:
					status_launch_game=self.click_button(405,630,470,663)
					status_launch_infos=self.click_button(20,296,672,756)
					if status_launch_game==True:
						index_game=1
					elif status_launch_infos==True:
						index_game=0
						
						
			clock.tick(60)
		pygame.quit()