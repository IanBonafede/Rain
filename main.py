import pygame 
import random

#we need this for every pygame program, to use the library
pygame.init() 

# create a screen variable with width and height
screenW = 800
screenH = 600
screen = pygame.display.set_mode([screenW, screenH])

numDots = 200

gravity = 0.5

# fill information arrays with 0, numDots of them
colors = [0]*numDots
radii = [0]*numDots
locations = [0]*numDots
speeds = [0]*numDots
bounced = [False]*numDots


# set the information to random values
for i in range(numDots): 
  colors[i] = [random.randint(0, 10) , random.randint(0, 10), random.randint(200, 255)]
  radii[i] = random.randint(1, 3)
  locations[i] = [random.randint(0 + radii[i], screenW - radii[i] ),  0]
  speeds[i] = [ random.randint(-1, 1), random.randint(0, 5)]



def updateDots():
  for i in range(numDots):
    # update speedx
    
    # update speedy
    speeds[i][1] += gravity
    
    if locations[i][1] + radii[i] > screenH:
      if bounced[i]:
        # reset drop
        locations[i] = [random.randint(0 + radii[i], screenW - radii[i] ),  0]
        speeds[i][1] =  random.randint(0, 5)
        bounced[i] = False
      else:
        speeds[i][1] = -speeds[i][1] / random.randint(3, 10)
        bounced[i] = True
    # update x location
    locations[i][0] += speeds[i][0]
    # update y location
    locations[i][1] += speeds[i][1]
    # draw circle
    pygame.draw.circle(screen, colors[i], locations[i], radii[i])




# Color is in RGB
# each value is 0-255
BLACK = (0, 0, 0)



# main loop for pygame
keep_going = True 

# control the fps
timer = pygame.time.Clock()

while keep_going:
  # loop through the events, check them and make sure 
  # what we want happens for each event
  for event in pygame.event.get():
    # if the event is quit
    if event.type == pygame.QUIT:
      #exit the loop
      keep_going = False 
  
  # before we draw everything else, fill black
  screen.fill(BLACK)

  # update dots and draw them
  updateDots()

  # update the display every frame
  pygame.display.update()

  # make the clock speed 60 fps
  timer.tick(60)

pygame.quit()



