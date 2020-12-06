import pygame, sys

class GameState():            
	def __init__(self):
		self.state = "intro"

	def intro(self):       
		screen = pygame.display.set_mode((width,height))
		screen_ = pygame.transform.scale(pygame.image.load("backround .png"), (width,height))
		screen.blit(screen_,(0, 0))

		vietname_button = pygame.transform.scale(pygame.image.load("english.png").convert_alpha(),(int(width/(5/2)), int(height/(11/2))))
		vietname_button_rect = vietname_button.get_rect(center = (int(width/(5/3)), int(height/(12/4))))

		english_button = pygame.transform.scale(pygame.image.load("tieng_viet.png").convert_alpha(),(int(width/(5/2)), int(height/(11/2))))
		english_button_rect = english_button.get_rect(center = (int(width/(5/3)), int(height/(13/9))))

		back_button= pygame.transform.scale(pygame.image.load("Nut-Quay-lai.jpg").convert_alpha(),(int(width/9), int(height/11)))
		back_button_rect = back_button.get_rect(center = (int(width - width/9), int(height/11)))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:      
				pos = pygame.mouse.get_pos()              
				if vietname_button_rect.collidepoint(pos):    
					self.state = "main_game_1"               
				if english_button_rect.collidepoint(pos):
					self.state = "main_game_2"
				if back_button_rect.collidepoint(pos):
					self.state = "back"
		
			
			screen.blit(vietname_button,vietname_button_rect)
			screen.blit(english_button,english_button_rect)
			screen.blit(back_button, back_button_rect)
		
			pygame.display.update()

	def main_game_1(self):            
		screen.fill((255,255,255))
		font = pygame.font.SysFont("Courier", 20)
		font = font.render("màng hình tiếng việt", False, (0, 128, 0))
		screen.blit(font, (100,200))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					self.state = "intro"

			pygame.display.update()

	def main_game_2(self):            
		screen.fill((255,255,255))
		font = pygame.font.SysFont("Courier", 20)
		font = font.render("màng hình game tiếng anh", False, (0, 128, 0))
		screen.blit(font, (100,200))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					self.state = "intro"

			pygame.display.update()

	def back(self):           
		screen.fill((0,0,0))
		font = pygame.font.SysFont("Courier", 20)
		font = font.render("Màng hình cũ đã định dạng sẵn khi vào game", False, (255, 255, 255))
		screen.blit(font, (100,200))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					self.state = "intro"

			pygame.display.update()

	def state_manager(self):             
		if self.state == "intro":       
			self.intro()
		if self.state == "main_game_1":    
			self.main_game_1()
		if self.state == "main_game_2":    
			self.main_game_2()
		if self.state == "back":     
			self.back()


pygame.init()
clock = pygame.time.Clock()

width = 800
height = 500

screen = pygame.display.set_mode((width, height))
screen.fill((255,255,255))
pygame.display.set_caption("Test")

game_state = GameState()      





while True:                          
	game_state.state_manager()
	clock.tick(30)      
