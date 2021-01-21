import pygame

# ----- CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
SKY_BLUE = (95, 165, 228)
GREEN = (96,171,154)
WIDTH = 1280
HEIGHT = 720
TITLE = "<Draven>"



class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()


        self.image = pygame.image.load("./images/draven.png")
        self.image = pygame.transform.scale(self.image, (258,181))
        self.rect = self.image.get_rect()

        # Sets sprite in the middle
        self.rect.centerx = (WIDTH//2)
        self.rect.centery = (HEIGHT//2)

        self.vel_x = 0
        self.vel_y = 0

    def update(self):

        # Moves left/right and up/down
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y


    def go_left(self):
        self.vel_x = -6

    def go_right(self):
        self.vel_x = 6

    def go_up(self):
        self.vel_y = -6

    def go_down(self):
        self.vel_y = 6

    def stop(self):
        self.vel_x = 0
        self.vel_y = 0




def main():
    pygame.init()

    # ----- SCREEN PROPERTIES
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(TITLE)

    # ----- LOCAL VARIABLES
    done = False
    clock = pygame.time.Clock()


    all_sprites_group = pygame.sprite.Group()

    # Player creation
    player = Player()
    all_sprites_group.add(player)

    # ----- MAIN LOOP
    while not done:
        # -- Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_UP:
                    player.go_up()
                if event.key == pygame.K_DOWN:
                    player.go_down()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.vel_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.vel_x > 0:
                    player.stop()
                if event.key == pygame.K_UP and player.vel_y < 0:
                    player.stop()
                if event.key == pygame.K_DOWN and player.vel_y > 0:
                    player.stop()






        # ----- LOGIC
        all_sprites_group.update()

        # ----- DRAW
        screen.fill(GREEN)
        all_sprites_group.draw(screen)

        # ----- UPDATE

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()