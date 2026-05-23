import  pygame, sys, random
pygame.init()

# Settup

Width = 500
Height = 400
screen = pygame.display.set_mode((Width,Height))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

#Game state

score, time_left = 0, 30
circle = [Width/2, Height/2, 30]

running = True
while running:
  screen.fill((255, 255, 255))
  for e in pygame.event.get():
    if e.type == pygame.QUIT: pygame.quit(); sys.exit()
    if e.type == pygame.MOUSEBUTTONDOWN:
      x,y = e.pos
      if (x-circle[0])**2 + (y-circle[1]**2) < circle[2] **2:
        score+=1
        circle = [random.randint(30,Width-30), random.randint(30,Height-30), 30]

    #Draw circles 
  pygame.draw.circle(screen, (255, 0, 0), (circle[0],circle[1]), circle[2])
  
  #Draw + score + timer
  screen.blit(font.render(f"Score:{score}",1,(0,0,0)),(10,10))
  screen.blit(font.render(f"Time:{time_left}",1,(0,0,0)),(Width - 120, 10))

  pygame.display.flip()
  clock.tick(60)

  #Countdown

  if pygame.time.get_ticks() % 1000 < 20: time_left -=1
  if time_left <= 0:
    screen.fill((255, 255, 255))
    screen.blit(font.render(f"Final Score: {score}", 1, (0,0,0)), (Width//2-100, Height//2))
    pygame.display.flip()
    pygame.time.wait(2000)
    break


