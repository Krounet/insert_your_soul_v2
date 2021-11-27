import pygame

class Loading_sprite():

	def launch_screen():
		#chargement elements de l'écran d'accueil
		load_elements={"bg":pygame.image.load("sprites\loading_screen\loading_screen.png"),"SOUL_1":pygame.image.load("sprites\loading_screen\SOUL_exec1.png"),
		"SOUL_2":pygame.image.load("sprites\loading_screen\SOUL_exec2.png"),"INFOS_1":pygame.image.load("sprites\loading_screen\INFOS1.png"),"INFOS_2":pygame.image.load("sprites\loading_screen\INFOS2.png")}
		load_elements["bg"].convert()
		load_elements["SOUL_1"].convert()
		load_elements["SOUL_2"].convert()
		load_elements["INFOS_1"].convert()
		load_elements["INFOS_2"].convert()
		return load_elements
	
	def game_screen():
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
		
		
	def infos_screen():
		#chargement éléments d'infos du jeu
		load_elements={"infos_screen":pygame.image.load("sprites\infos_screen\INFOSscreen.png").convert()}
		return load_elements