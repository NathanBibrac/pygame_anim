import pygame
import random
import math
import matplotlib.pyplot as plt 

pi = math.pi
sin = lambda x: math.sin(x)

step = pi/1200

X = [step*i for i in range(2400)]
Y = [255*(sin(x)+1)/2 for x in X]



# Initialize pygame and create a window
pygame.init()
info = pygame.display.Info()
screen = pygame.display.set_mode((info.current_w, info.current_h), pygame.FULLSCREEN) #, screen_num=1

# Create a list to store the circles
objects = []

# Create a class for the circles
class Object:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.color_r = random.randint(1,119)
        self.color_g = random.randint(1,119)
        self.color_b = random.randint(1,119)
        self.color = (Y[self.color_r],Y[self.color_g],Y[self.color_b])
        self.speed_x = random.randint(-5, 5)
        self.speed_y = random.randint(-5, 5)
        self.growth_rate = random.uniform(0.1, 0.5)

    def move(self):
        # Move the circle and rebound off the edges of the screen
        self.x += self.speed_x
        self.y += self.speed_y
        if self.x < 0 or self.x > info.current_w:
            self.speed_x = -self.speed_x
        if self.y < 0 or self.y > info.current_h:
            self.speed_y = -self.speed_y
        # self.speed_x = self.speed_x * random.uniform(0.8, 1.2)
        # self.speed_y = self.speed_y * random.uniform(0.8, 1.2)

    def grow(self):
        # Increase the size of the circle
        self.size += self.growth_rate
        if self.size > 100:
            self.growth_rate = -self.growth_rate
        elif self.size < 20:
            self.growth_rate = abs(self.growth_rate)

    def change_color(self):
        # Change the color of the circle
        self.color_r = (self.color_r+1)%119
        self.color_g = (self.color_g+1)%119
        self.color_b = (self.color_b+1)%119

        self.color = (Y[self.color_r],Y[self.color_g],Y[self.color_b])
        

        


class Circle(Object):
    def draw(self):
        # Draw the circle on the screen
        pygame.draw.circle(screen, (self.color_r,self.color_g,self.color_b),(int(self.x), int(self.y)),int(self.size))

class Rectangle(Object):
    def draw(self):
        # Draw rectangle on the screen
        pygame.draw.rect(screen,  (int(self.x), int(self.y), int(self.size), int(self.size)))
        
class Ellipse(Object):
    def draw(self):
        # Draw the ellipse on the screen
        pygame.draw.ellipse(screen,(int(self.x), int(self.y), int(self.size), int(self.size)))


def main():
    # Create some initial circles
    for i in range(50):
        x = random.randint(0, info.current_w)
        y = random.randint(0, info.current_h)
        size = random.randint(10, 50)
        objects.append(Circle(x, y, size))
        # color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    '''
    # Create some initial rectangles
    for i in range(20):
        x = random.randint(0, info.current_w)
        y = random.randint(0, info.current_h)
        size = random.randint(10, 50)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        objects.append(Rectangle(x, y, size, color))
    
    # Create some initial ellipses
    for i in range(20):
        x = random.randint(0, info.current_w)
        y = random.randint(0, info.current_h)
        size = random.randint(10, 50)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        objects.append(Ellipse(x, y, size, color))
    '''
    life = 0

    # Main game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame. K_ESCAPE:
                    running = False

        # Clear the screen
        screen.fill((0, 0, 0))
        

        # Move and grow the circles, then draw them
        for object in objects:
            object.move()
            object.grow()
            object.draw()
            object.change_color()

        life = (life+1)%120

        # Update the display
        pygame.display.flip()

        # Wait for a bit
        pygame.time.wait(10)

    # Clean up
    pygame.quit()

if __name__ == "__main__":
    main()
