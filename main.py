import pygame
import random

# ----- CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
SKY_BLUE = (95, 165, 228)
GREEN = (96, 171, 154)
WIDTH = 1920
HEIGHT = 1080
NUM_ENEMIES = 20
TITLE = "<Draven>"

font_name = pygame.font.match_font('arial')


def score_board(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("./images/background.jpg")
        self.image = pygame.transform.scale(self.image, (WIDTH, HEIGHT))

        self.rect = self.image.get_rect()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("./images/draven.png")
        #self.image = pygame.transform.scale(self.image, (258, 181))
        self.rect = self.image.get_rect()

        # Sets sprite location
        self.rect.centerx = (WIDTH // 10)
        self.rect.centery = (HEIGHT // 2)

        self.vel_x = 0
        self.vel_y = 0

    def update(self):
        # Moves left/right and up/down
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

    def go_left(self):
        self.vel_x = -8
        self.image = pygame.image.load("./images/dravenflipped.png")

    def go_right(self):
        self.vel_x = 8
        self.image = pygame.image.load("./images/draven.png")

    def go_leftw(self):
        self.vel_x = -15
        self.image = pygame.image.load("./images/dravenflipped.png")

    def go_rightw(self):
        self.vel_x = 15
        self.image = pygame.image.load("./images/draven.png")

    def go_up(self):
        self.vel_y = -8

    def go_down(self):
        self.vel_y = 8

    def stop(self):
        self.vel_x = 0
        self.vel_y = 0


class Axe(pygame.sprite.Sprite):
    def __init__(self, coords):
        super().__init__()

        self.image = pygame.image.load("./images/axe.png")
        self.image = pygame.transform.scale(self.image, (100, 140))

        self.rect = self.image.get_rect()
        self.rect.centerx, self.rect.bottom = coords

        self.vel_x = 0

    def update(self):
        self.rect.x += self.vel_x


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x_coord, y_coord, vel_x, vel_y):
        super().__init__()

        self.image = pygame.image.load("./images/minion.png")
        self.image = pygame.transform.scale(self.image, (105, 86))

        self.rect = self.image.get_rect()

        self.vel_x = vel_x
        self.vel_y = vel_y

        self.rect.centerx = (x_coord)
        self.rect.centery = (y_coord)

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        # if self.rect.right > WIDTH or self.rect.left < 0:
        # self.vel_x *= -1


class Teemo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("./images/teemo.png")
        self.image = pygame.transform.scale(self.image, (137, 192))
        self.rect = self.image.get_rect()

        self.rect.centerx = WIDTH + 200
        self.rect.centery = HEIGHT // 2

        self.vel_x = 0
        self.vel_y = 0

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y


        if self.rect.y > HEIGHT or self.rect.y < 0:
            self.vel_y *= -1

    def stop(self):
        self.vel_x = 0


class Mushroom(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("./images/mushroom.png")
        self.image = pygame.transform.scale(self.image, (50, 100))
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
    score = 10
    health = 1000
    bool = True

    # ---- SPRITE GROUPS

    all_sprites_group = pygame.sprite.Group()
    background_group = pygame.sprite.Group()
    axe_sprites = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()

    # Player creation
    player = Player()
    all_sprites_group.add(player)

    # Minion creation
    for i in range(NUM_ENEMIES):
        enemy = Enemy(random.randrange(WIDTH, WIDTH * 3), random.randrange(50, HEIGHT), random.randrange(-2, -1), 0)
        all_sprites_group.add(enemy)
        enemy_group.add(enemy)

    # Stronger enemy creation
    teemo = Teemo()
    all_sprites_group.add(teemo)

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
                    bool = True
                if event.key == pygame.K_LEFT:
                    player.go_left()
                    bool = False
                if event.key == pygame.K_UP:
                    player.go_up()
                if event.key == pygame.K_DOWN:
                    player.go_down()

                # Abilities
                if event.key == pygame.K_q and bool:
                    axe = Axe(player.rect.midbottom)
                    all_sprites_group.add(axe)
                    axe_sprites.add(axe)
                    axe.vel_x = 8
                if event.key == pygame.K_q and not bool:
                    axe = Axe(player.rect.midbottom)
                    all_sprites_group.add(axe)
                    axe_sprites.add(axe)
                    axe.vel_x = -8
                if event.key == pygame.K_w and pygame.K_RIGHT and bool:
                    player.go_rightw()
                if event.key == pygame.K_w and pygame.K_LEFT and not bool:
                    player.go_leftw()

                # TODO: Add other abilities
                # TODO: Rotate the axe
                # TODO: Create stronger minion waves

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.vel_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.vel_x > 0:
                    player.stop()
                if event.key == pygame.K_UP and player.vel_y < 0:
                    player.stop()
                if event.key == pygame.K_DOWN and player.vel_y > 0:
                    player.stop()
                if event.key == pygame.K_w and player.vel_x > 0:
                    player.stop()
                if event.key == pygame.K_w and player.vel_x < 0:
                    player.stop()

        # Makes sure player is not out of screen (x-axis)
        if player.rect.right > WIDTH:
            player.rect.right = WIDTH
        if player.rect.left < 0:
            player.rect.left = 0

        # Makes sure player is not out of screen (y-axis)
        if player.rect.bottom > HEIGHT:
            player.rect.bottom = HEIGHT
        if player.rect.top < 0:
            player.rect.top = 0

        # ----- LOGIC
        all_sprites_group.update()

        # Check if axe collided with enemy

        for axe in axe_sprites:

            if axe.rect.right > WIDTH:
                axe.kill()

            enemy_hit_group = pygame.sprite.spritecollide(axe, enemy_group, True)
            if len(enemy_hit_group) > 0:
                axe.kill()
            for i in enemy_hit_group:
                score += 20

        for enemy in enemy_group:

            enemy_hit_player_group = pygame.sprite.spritecollide(player, enemy_group, True)
            for i in enemy_hit_player_group:
                score += 10
                health -= 50
                print(health)

            # Stronger Enemy
            if score >= 2:
                teemo.vel_x = -5
            if teemo.rect.centerx == WIDTH - 200:
                teemo.stop()
                teemo.vel_y = 4
            if teemo.rect.y > HEIGHT or teemo.rect.y < 0:
                teemo.vel_y *= -1

        # ----- DRAW
        background_group.draw(screen)
        all_sprites_group.draw(screen)

        score_board(screen, f"Score: {score}", 50, WIDTH - 100, 10)
        score_board(screen, f"Health: {health}", 50, WIDTH - 350, 10)

        # ----- UPDATE
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
