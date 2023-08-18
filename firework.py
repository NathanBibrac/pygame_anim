import pygame
import time
import random

# Initialize pygame and create a window
pygame.init()
info = pygame.display.Info()
screen = pygame.display.set_mode((info.current_w, info.current_h), pygame.FULLSCREEN) 
pygame.display.set_caption("Pygame Template")
clock = pygame.time.Clock()

fireworks = []

class Firework:
    def __init__(self, x, y, color, size, speed_x, speed_y, gravity):
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.gravity = gravity
        self.particles = []
        self.life = 0

    def explode(self):
        for i in range(self.size):
            particle_x = self.x + random.uniform(-self.size/2, self.size/2)
            particle_y = self.y + random.uniform(-self.size/2, self.size/2)
            particle_color = self.color
            particle_size = random.randint(1, 3)
            particle_speed_x = random.uniform(-2, 2)
            particle_speed_y = random.uniform(-2, 2)
            particle = Particle(particle_x, particle_y, particle_color, particle_size, particle_speed_x, particle_speed_y)
            self.particles.append(particle)

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.speed_y += self.gravity
        for particle in self.particles:
            particle.update()
            particle.draw()

    def check_life(self):
        self.life += 1
        if self.life >= 100:
            self.particles = []
            fireworks.remove(self)



class Particle:
    def __init__(self, x, y, color, size, speed_x, speed_y):
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        self.speed_x = speed_x
        self.speed_y = speed_y

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size)


def create_firework(amount):
    # Create some initial fireworks
    for i in range(amount):
        x = random.randint(0, info.current_w)
        y = random.randint(0, info.current_h) #random.randint(info.current_h, info.current_h*2)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        size = random.randint(10, 20)
        speed_x = random.uniform(-2, 2)
        speed_y = random.uniform(-15, -10)
        gravity = 0.3
        firework = Firework(x, y, color, size, speed_x, speed_y, gravity)
        firework.explode()
        fireworks.append(firework)

    return fireworks

def main():


    # Main game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # Clear the screen
        screen.fill((0, 0, 0))

        fireworks = create_firework(5)

        # Update and draw the fireworks
        for firework in fireworks:
            firework.update()
            firework.check_life()

        # Update the display
        pygame.display.flip()

        # Wait for a bit
        pygame.time.wait(10)

    # Clean up
    pygame.quit()

if __name__ == "__main__":
    main()

