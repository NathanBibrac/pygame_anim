import pygame
import random

def main():
    # Initialize pygame and create a window
    pygame.init()
    info = pygame.display.Info()
    screen = pygame.display.set_mode((info.current_w, info.current_h), pygame.FULLSCREEN)
    pygame.display.set_caption("Matrix animation")

    # Create a list of characters
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789?./!:;()[]<>*&^%$#@"

    # Create a clock for controlling the frame rate
    clock = pygame.time.Clock()

    # Create a list to store the columns of characters
    columns = []

    # Create a class for the columns of characters
    class Column:
        def __init__(self, x):
            self.x = x
            self.characters = []
            for i in range(info.current_h // 30):
                self.characters.append(random.choice(characters))

        def move(self):
            # Move the column of characters
            #self.x -= 1
            pass

            # Add a new character to the top of the column
            self.characters.pop(0)
            self.characters.append(random.choice(characters))

        def draw(self):
            # Draw the column of characters on the screen
            for i, c in enumerate(self.characters):
                text_surface = font.render(c, True, (0, 255, 0))
                text_rect = text_surface.get_rect()
                text_rect.x = self.x
                text_rect.y = i * 30
                screen.blit(text_surface, text_rect)

    # Create a font for the characters
    font = pygame.font.SysFont("Consolas", 30)

    # Create the columns of characters
    for i in range(info.current_w // 30):
        columns.append(Column(i * 30))

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # Clear the screen
        screen.fill((0, 0, 0))

        # Move and draw the columns of characters
        for column in columns:
            column.move()
            column.draw()

        # Update the display
        pygame.display.flip()

        # Wait for a bit
        pygame.time.wait(10)

        # Control the frame rate
        clock.tick(80)

    # Clean up
    pygame.quit()

if __name__ == "__main__":
    main()
