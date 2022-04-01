import pygame
pygame.init()
win=pygame.display.set_mode((550,650))
base_font=pygame.font.Font(None,80)
user_text=""
pygame.display.set_caption("tic tac toe numbers")
first=pygame.draw.rect(win,(255,255,255),(25,25,150,150))
second=pygame.draw.rect(win,(255,255,255),(200,25,150,150))
third=pygame.draw.rect(win,(255,255,255),(375,25,150,150))
fourth=pygame.draw.rect(win,(255,255,255),(25,200,150,150))
fifth=pygame.draw.rect(win,(255,255,255),(200,200,150,150))
sixth=pygame.draw.rect(win,(255,255,255),(375,200,150,150))
seventh=pygame.draw.rect(win,(255,255,255),(25,375,150,150))
eighth=pygame.draw.rect(win,(255,255,255),(200,375,150,150))
ninth=pygame.draw.rect(win,(255,255,255),(375,375,150,150))
state=pygame.draw.rect(win,(0,0,255),(25,550,500,100))
run=True
n=0
a=True
b=True
c=True
d=True
e=True
f=True
g=True
h=True
i=True


text1=""
text2=""
text3=""
text4=""
text5=""
text6=""
text7=""
text8=""
text9=""

x=0
game=True
def check_winner(game):
	if r1+r2+r3==15 and player1==True :
		state=pygame.draw.rect(win,(0,0,255),(25,550,500,100))


		text_surface = base_font.render(text1, True, (51, 255, 51))
		win.blit(text_surface, (25, 25))

		text_surface = base_font.render(text2, True, (51, 255, 51))
		win.blit(text_surface, (200, 25))

		text_surface = base_font.render(text3, True, (51, 255, 51))
		win.blit(text_surface, (375, 25))



		font=pygame.font.SysFont("Times New Roman",40,True,False)
		surface1=font.render("player1 won",True,(255,0,0))
		win.blit(surface1,(0,550))
		game =False
		return False

	elif r4+r5+r6==15 and player1==True:
		state=pygame.draw.rect(win,(0,0,255),(25,550,500,100))

		text_surface = base_font.render(text4, True, (51, 255, 51))

		win.blit(text_surface, (25, 200))

		text_surface = base_font.render(text5, True, (51, 255, 51))

		win.blit(text_surface, (200, 200))

		text_surface = base_font.render(text6, True, (51, 255, 51))

		win.blit(text_surface, (375, 200))



		font=pygame.font.SysFont("Times New Roman",40,True,False)
		surface1=font.render("player1 won",True,(0,0,0))
		win.blit(surface1,(25,550))



		game=False
		return False
	elif r7+r8+r9==15 and player1==True :
		state=pygame.draw.rect(win,(0,0,255),(25,550,500,100))

		text_surface = base_font.render(text7, True, (51, 255, 51))

		win.blit(text_surface, (25, 375))

		text_surface = base_font.render(text8, True, (51, 255, 51))

		win.blit(text_surface, (200, 375))

		text_surface = base_font.render(text9, True, (51, 255, 51))

		win.blit(text_surface, (375, 375))


		font=pygame.font.SysFont("Times New Roman",40,True,False)
		surface1=font.render("player1 won",True,(255,0,0))
		win.blit(surface1,(25,550))
		game=False
		return False
	elif r1+r4+r7==15 and player1==True :
		state=pygame.draw.rect(win,(0,0,255),(25,550,500,100))

		text_surface = base_font.render(text1, True, (51, 255, 51))
		win.blit(text_surface, (25, 25))

		text_surface = base_font.render(text4, True, (51, 255, 51))

		win.blit(text_surface, (25, 200))

		text_surface = base_font.render(text7, True, (51, 255, 51))

		win.blit(text_surface, (25, 375))
		state=pygame.draw.rect(win,(0,0,255),(25,550,500,100))



		font=pygame.font.SysFont("Times New Roman",40,True,False)
		surface1=font.render("player1 won",True,(255,0,0))
		win.blit(surface1,(25,550))

		return False
	elif r2+r5+r8==15 and player1==True :
		state=pygame.draw.rect(win,(0,0,255),(25,550,500,100))

		text_surface = base_font.render(text2, True, (51, 255, 51))
		win.blit(text_surface, (200, 25))

		text_surface = base_font.render(text5, True, (51, 255, 51))

		win.blit(text_surface, (200, 200))

		text_surface = base_font.render(text8, True, (51, 255, 51))

		win.blit(text_surface, (200, 375))
		state=pygame.draw.rect(win,(0,0,255),(25,550,500,100))

		font=pygame.font.SysFont("Times New Roman",40,True,False)
		surface1=font.render("player1 won",True,(255,0,0))
		win.blit(surface1,(25,550))


		game=False
		return False
	elif r3+r6+r9==15 and player1==True :
		state=pygame.draw.rect(win,(0,0,255),(25,550,500,100))

		text_surface = base_font.render(text3, True, (51, 255, 51))
		win.blit(text_surface, (375, 25))

		text_surface = base_font.render(text6, True, (51, 255, 51))

		win.blit(text_surface, (375, 200))

		text_surface = base_font.render(text9, True, (51, 255, 51))

		win.blit(text_surface, (375, 375))
		state=pygame.draw.rect(win,(0,0,255),(25,550,500,100))



		font=pygame.font.SysFont("Times New Roman",40,True,False)
		surface1=font.render("player1 won",True,(255,0,0))
		win.blit(surface1,(25,550))

		game=False
		return False
	elif r1 + r5 + r9 == 15 and player1 == True :
		state=pygame.draw.rect(win,(0,0,255),(25,550,500,100))

		text_surface = base_font.render(text1, True, (51, 255, 51))
		win.blit(text_surface, (25, 25))

		text_surface = base_font.render(text5, True, (51, 255, 51))

		win.blit(text_surface, (200, 200))

		text_surface = base_font.render(text9, True, (51, 255, 51))

		win.blit(text_surface, (375, 375))
		state=pygame.draw.rect(win,(0,0,255),(25,550,500,100))

		font=pygame.font.SysFont("Times New Roman",40,True,False)
		surface1=font.render("player2 won",True,(255,0,0))
		win.blit(surface1,(25,550))
		game=False
		return False
	elif r3+r5+r7==15 and player1==True :
		state=pygame.draw.rect(win,(0,0,255),(25,550,500,100))

		text_surface = base_font.render(text5, True, (51, 255, 51))

		win.blit(text_surface, (200, 200))

		text_surface = base_font.render(text3, True, (51, 255, 51))
		win.blit(text_surface, (375, 25))

		text_surface = base_font.render(text7, True, (51, 255, 51))

		win.blit(text_surface, (25, 375))
		state=pygame.draw.rect(win,(0,0,255),(25,550,500,100))

		font=pygame.font.SysFont("Times New Roman",40,True,False)
		surface1=font.render("player2 won",True,(255,0,0))
		win.blit(surface1,(25,550))


		game=False
		return False

	elif r1+r2+r3==15 and player1==False :
		state=pygame.draw.rect(win,(0,0,255),(25,550,500,100))

		text_surface = base_font.render(text1, True, (51, 255, 51))
		win.blit(text_surface, (25, 25))

		text_surface = base_font.render(text2, True, (51, 255, 51))
		win.blit(text_surface, (200, 25))

		text_surface = base_font.render(text3, True, (51, 255, 51))
		win.blit(text_surface, (375, 25))
		state=pygame.draw.rect(win,(0,0,255),(25,550,500,100))



		font=pygame.font.SysFont("Times New Roman",40,True,False)
		surface1=font.render("player2 won",True,(255,0,0))
		win.blit(surface1,(25,550))



		game= False
		return False

	elif r4+r5+r6==15 and player1==False :
		state=pygame.draw.rect(win,(0,0,255),(25,550,500,100))

		text_surface = base_font.render(text4, True, (51, 255, 51))

		win.blit(text_surface, (25, 200))

		text_surface = base_font.render(text5, True, (51, 255, 51))

		win.blit(text_surface, (200, 200))

		text_surface = base_font.render(text6, True, (51, 255, 51))

		win.blit(text_surface, (375, 200))



		font=pygame.font.SysFont("Times New Roman",40,True,False)
		surface1=font.render("player2 won",True,(255,0,0))
		win.blit(surface1,(25,550))

		game=False
		return False
	elif r7+r8+r9==15 and player1==False:
		state=pygame.draw.rect(win,(0,0,255),(25,550,500,100))
		text_surface = base_font.render(text7, True, (51, 255, 51))

		win.blit(text_surface, (25, 375))

		text_surface = base_font.render(text8, True, (51, 255, 51))

		win.blit(text_surface, (200, 375))

		text_surface = base_font.render(text9, True, (51, 255, 51))

		win.blit(text_surface, (375, 375))

		font=pygame.font.SysFont("Times New Roman",40,True,False)
		surface1=font.render("player2 won",True,(255,0,0))
		win.blit(surface1,(25,550))
		game=False
		return False
	elif r1+r4+r7==15 and player1==False:
		state=pygame.draw.rect(win,(0,0,255),(25,550,500,100))
		text_surface = base_font.render(text1, True, (51, 255, 51))
		win.blit(text_surface, (25, 25))

		text_surface = base_font.render(text4, True, (51, 255, 51))

		win.blit(text_surface, (25, 200))

		text_surface = base_font.render(text7, True, (51, 255, 51))

		win.blit(text_surface, (25, 375))

		font=pygame.font.SysFont("Times New Roman",40,True,False)
		surface1=font.render("player2 won",True,(255,0,0))
		win.blit(surface1,(25,550))

		game=False
		return False
	elif r2+r5+r8==15 and player1==False:
		state=pygame.draw.rect(win,(0,0,255),(25,550,500,100))
		text_surface = base_font.render(text2, True, (51, 255, 51))
		win.blit(text_surface, (200, 25))

		text_surface = base_font.render(text5, True, (51, 255, 51))

		win.blit(text_surface, (200, 200))

		text_surface = base_font.render(text8, True, (51, 255, 51))

		win.blit(text_surface, (200, 375))

		font=pygame.font.SysFont("Times New Roman",40,True,False)
		surface1=font.render("player2 won",True,(255,0,0))
		win.blit(surface1,(25,550))
		game=False
		return False
	elif r3+r6+r9==15 and player1==False:
		state=pygame.draw.rect(win,(0,0,255),(25,550,500,100))
		text_surface = base_font.render(text3, True, (51, 255, 51))
		win.blit(text_surface, (375, 25))

		text_surface = base_font.render(text6, True, (51, 255, 51))

		win.blit(text_surface, (375, 200))

		text_surface = base_font.render(text9, True, (51, 255, 51))

		win.blit(text_surface, (375, 375))

		font=pygame.font.SysFont("Times New Roman",40,True,False)
		surface1=font.render("player2 won",True,(255,0,0))
		win.blit(surface1,(25,550))
		game=False
		return False
	elif r1 + r5 + r9 == 15 and player1 == False:
		state=pygame.draw.rect(win,(0,0,255),(25,550,500,100))
		text_surface = base_font.render(text1, True, (51, 255, 51))
		win.blit(text_surface, (25, 25))

		text_surface = base_font.render(text5, True, (51, 255, 51))

		win.blit(text_surface, (200, 200))

		text_surface = base_font.render(text9, True, (51, 255, 51))

		win.blit(text_surface, (375, 375))

		font=pygame.font.SysFont("Times New Roman",40,True,False)
		surface1=font.render("player2 won",True,(255,0,0))
		win.blit(surface1,(25,550))
		game=False
		return False
	elif r3+r5+r7==15 and player1==False:
		state=pygame.draw.rect(win,(0,0,255),(25,550,500,100))
		text_surface = base_font.render(text5, True, (51, 255, 51))

		win.blit(text_surface, (200, 200))

		text_surface = base_font.render(text3, True, (51, 255, 51))
		win.blit(text_surface, (375, 25))

		text_surface = base_font.render(text7, True, (51, 255, 51))

		win.blit(text_surface, (25, 375))

		font=pygame.font.SysFont("Times New Roman",40,True,False)
		surface1=font.render("player2 won",True,(255,0,0))
		win.blit(surface1,(25,550))



		game=False
		return False
	else:
		return True




player1=True


r1,r2,r3,r4,r5,r6,r7,r8,r9=20,20,20,20,20,20,20,20,20



while run:
	pygame.time.delay(100)
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run=False
		if event.type==pygame.MOUSEBUTTONUP:
			pos=pygame.mouse.get_pos()
		if event.type==pygame.KEYDOWN:
			text=event .unicode

			if first.collidepoint(pos) and a==True :
				state=pygame.draw.rect(win,(0,0,255),(25,550,500,100))
				font = pygame.font.SysFont("Times New Roman", 40, True, False)
				surface1 = font.render("player1 turn", True, (255, 0, 0))
				win.blit(surface1, (25,550))
				text1+=event .unicode

				text_surface = base_font.render(text1, True, (255, 0, 0))
				win.blit(text_surface, (25, 25))
				r1=int(text1)
				n+=1
				check_winner(game)
				a=False
			if   second.collidepoint(pos) and b==True :
				state=pygame.draw.rect(win,(0,0,255),(25,550,500,100))
				text2=event .unicode
				text_surface = base_font.render(text2, True, (255, 0, 0))

				win.blit(text_surface,(200, 25))
				r2=int(text2)
				if r2 %2==0:
					state=pygame.draw.rect(win,(0,0,255),(25,550,500,100))
					font = pygame.font.SysFont("Times New Roman", 40, True, False)
					surface1 = font.render("player1 turn", True, (255, 0, 0))
					win.blit(surface1, (25,550))
					player1=True

				else:
					state=pygame.draw.rect(win,(0,0,255),(25,550,500,100))
					font = pygame.font.SysFont("Times New Roman", 40, True, False)
					surface1 = font.render("player2 turn", True, (255, 0, 0))
					win.blit(surface1, (25,550))
					player1=False
				n += 1
				check_winner(game)
				b=False

			if   third.collidepoint(pos) and c==True :
				state=pygame.draw.rect(win,(0,0,255),(25,550,500,100))
				text3+=event .unicode
				text_surface = base_font.render(text3, True, (255, 0, 0))

				win.blit(text_surface, (375, 25))
				r3=int(text3)
				if r3 %2==0:
					state=pygame.draw.rect(win,(0,0,255),(25,550,500,100))
					font = pygame.font.SysFont("Times New Roman", 40, True, False)
					surface1 = font.render("player1 turn", True, (255, 0, 0))
					win.blit(surface1, (25,550))
					player1=True
				else:
					state=pygame.draw.rect(win,(0,0,255),(25,550,500,100))
					font = pygame.font.SysFont("Times New Roman", 40, True, False)
					surface1 = font.render("player2 turn", True, (255, 0, 0))
					win.blit(surface1, (25 ,550))
					player1=False
				n += 1
				check_winner(game)
				c=False
			if   fourth.collidepoint(pos) and d==True :
				state=pygame.draw.rect(win,(0,0,255),(25,550,500,100))
				text4+=event .unicode
				text_surface = base_font.render(text4, True, (255, 0, 0))

				win.blit(text_surface, (25, 200))
				r4=int(text4)
				if r4 %2==0:
					font = pygame.font.SysFont("Times New Roman", 40, True, False)
					surface1 = font.render("player1 turn", True, (255, 0, 0))
					win.blit(surface1, (25,550))
					player1=True
				else:
					font = pygame.font.SysFont("Times New Roman", 40, True, False)
					surface1 = font.render("player2 turn", True, (255, 0, 0))
					win.blit(surface1, (25,550))
					player1=False
				n += 1
				check_winner(game)
				d=False
			if   fifth.collidepoint(pos) and e==True :
				state=pygame.draw.rect(win,(0,0,255),(25,550,500,100))
				text5+=event .unicode
				text_surface = base_font.render(text5, True, (255, 0, 0))

				win.blit(text_surface, (200, 200))
				r5=int(text5)
				if r5 %2==0:
					font = pygame.font.SysFont("Times New Roman", 40, True, False)
					surface1 = font.render("player1 turn", True, (255, 0, 0))
					win.blit(surface1, (25,550))
					player1=True
				else:
					font = pygame.font.SysFont("Times New Roman", 40, True, False)
					surface1 = font.render("player2 turn", True, (255, 0, 0))
					win.blit(surface1, (25,550))
					player1=False
				n += 1
				check_winner(game)
				e=False
			if   sixth.collidepoint(pos) and f==True :
				state=pygame.draw.rect(win,(0,0,255),(25,550,500,100))
				text6+=event .unicode
				text_surface = base_font.render(text6, True, (255, 0, 0))

				win.blit(text_surface, (375, 200))
				r6=int(text6)

				if r6%2==0:
					font = pygame.font.SysFont("Times New Roman", 40, True, False)
					surface1 = font.render("player1 turn", True, (255, 0, 0))
					win.blit(surface1, (25,550))
					player1=True
				else:
					font = pygame.font.SysFont("Times New Roman", 40, True, False)
					surface1 = font.render("player2 turn", True, (255, 0, 0))
					win.blit(surface1, (25,550))
					player1=False


				n += 1
				check_winner(game)
				f=False
			if   seventh.collidepoint(pos) and g==True :
				state=pygame.draw.rect(win,(0,0,255),(25,550,500,100))
				text7+=event .unicode
				text_surface = base_font.render(text7, True, (255, 0, 0))

				win.blit(text_surface, (25, 375))
				r7=int(text7)
				if r7 %2==0:
					font = pygame.font.SysFont("Times New Roman", 40, True, False)
					surface1 = font.render("player1 turn", True, (255, 0, 0))
					win.blit(surface1, (25,550))
					player1=True
				else:
					font = pygame.font.SysFont("Times New Roman", 40, True, False)
					surface1 = font.render("player2 turn", True, (255, 0, 0))
					win.blit(surface1, (25,550))
					player1=False


				n += 1
				check_winner(game)
				g=False
			if   eighth.collidepoint(pos) and h==True :
				state=pygame.draw.rect(win,(0,0,255),(25,550,500,100))
				text8+=event .unicode
				text_surface = base_font.render(text8, True, (255, 0, 0))

				win.blit(text_surface, (200, 375))
				r8=int(text8)
				if r8 %2==0:
					font = pygame.font.SysFont("Times New Roman", 40, True, False)
					surface1 = font.render("player1 turn", True, (255, 0, 0))
					win.blit(surface1, (25 ,550))
					player1=True
				else:
					font = pygame.font.SysFont("Times New Roman", 40, True, False)
					surface1 = font.render("player2 turn", True, (255, 0, 0))
					win.blit(surface1, (25,550))
					player1=False
				n += 1
				check_winner(game)
				h=False
			if   ninth.collidepoint(pos) and i==True :
				state=pygame.draw.rect(win,(0,0,255),(25,550,500,100))
				text9+=event .unicode
				text_surface = base_font.render(text9, True, (255, 0, 0))

				win.blit(text_surface, (375, 375))
				r9=int(text9)
				if r9 %2==0:
					font = pygame.font.SysFont("Times New Roman", 40, True, False)
					surface1 = font.render("player1 turn", True, (255, 0, 0))
					win.blit(surface1, (25 ,560))
					player1=True
				else:
					font = pygame.font.SysFont("Times New Roman", 40, True, False)
					surface1 = font.render("player2 turn", True, (255, 0, 0))
					win.blit(surface1, (25 ,550))
					player1=False
				n += 1
				check_winner(game)
				i=False

		if check_winner(game)==True and x==0:
			pygame.display.update()
		elif check_winner(game)==False and x==0:
			pygame.display.update()
			x+=1
		
pygame.quit()
