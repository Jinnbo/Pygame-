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

        #if self.rect.x + self.rect.width > WIDTH or self.rect.x < 0:
        #    self.vel_x += 1
        #if self.rect.y + self.rect.height > HEIGHT or self.rect.y < 0:
        #    self.vel_y *= -1

        #TODO: Add boundaries around the screen


    def go_left(self):
        self.vel_x = -10

    def go_right(self):
        self.vel_x = 10

    def go_up(self):
        self.vel_y = -10

    def go_down(self):
        self.vel_y = 10

    def stop(self):
        self.vel_x = 0
        self.vel_y = 0


class Axe(pygame.sprite.Sprite):
    def __init__(self,coords):
        super().__init__()

        self.image = pygame.image.load("./images/axe.png")
        self.image = pygame.transform.scale(self.image, (180, 100))
        self.rect = self.image.get_rect()

        self.rect.centerx, self.rect.bottom = coords


        self.vel_x = 0


    def update(self):
        self.rect.x += self.vel_x

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("./images/enemy.png")
        self.image = pygame.transform.scale(self.image, (200,170))
        self.rect = self.image.get_rect()

        self.rect.centerx = (100)
        self.rect.centery = (HEIGHT // 2)

        self.vel_x = 0

    def update(self):
        self.rect.x += self.vel_x

class Enemylaser(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("./images/laser.png")
        self.image = pygame.transform.scale(self.image, (136,72))
        self.rect = self.image.get_rect()

class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("./images/background .png")
        self.image = pygame.transform.scale(self.image, (1280, 720))
        self.rect = self.image.get_rect()



def main():
    pygame.init()

    # ----- SCREEN PROPERTIES
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(TITLE)

    # ----- LOCAL VARIABLES
    done = False
    clock = pygame.time.Clock()
    b = True



    all_sprites_group = pygame.sprite.Group()
    background_group = pygame.sprite.Group()

    # Player creation
    player = Player()
    all_sprites_group.add(player)

    # Enemy creation
    enemy = Enemy()
    all_sprites_group.add(enemy)

    # Background creation
    background = Background()
    background_group.add(background)

    # ----- MAIN LOOP
    while not done:
        # -- Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                    player.image = pygame.image.load("./images/draven.png")
                    player.image = pygame.transform.scale(player.image, (258, 181))
                    b = True
                if event.key == pygame.K_LEFT:
                    player.go_left()
                    player.image = pygame.image.load("./images/dravenflip.png")
                    player.image = pygame.transform.scale(player.image, (258, 181))
                    b = False
                if event.key == pygame.K_UP:
                    player.go_up()
                if event.key == pygame.K_DOWN:
                    player.go_down()


                if event.key == pygame.K_q and b == True:
                    axe = Axe(player.rect.midright)
                    all_sprites_group.add(axe)
                    axe.image = pygame.image.load("./images/axe.png")
                    axe.image = pygame.transform.scale(axe.image, (180, 100))
                    axe.vel_x = 5
                if event.key == pygame.K_q and b == False:
                    axe = Axe(player.rect.midleft)
                    all_sprites_group.add(axe)
                    axe.image = pygame.image.load("./images/axeflip.png")
                    axe.image = pygame.transform.scale(axe.image, (180, 100))
                    axe.vel_x = -5





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
        background_group.draw(screen)
        all_sprites_group.draw(screen)

        # ----- UPDATE

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()