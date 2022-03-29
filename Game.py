import pygame, random

pygame.init()
running = True

screen_width = 1000
screen_height = 700

screen = pygame.display.set_mode((screen_width, screen_height))

score = {'box': 0, 'box2': 0}

# I should probably figure out how to import these images more efficiently haha

myfont = pygame.font.Font('my_font.ttf', 40)

food_img = pygame.image.load('Images/strawberry.png')
food_img = pygame.transform.scale(food_img, (64, 64))

player_orange_left = pygame.image.load('Images/orange_left.png')
player_orange_left = pygame.transform.scale(player_orange_left, (100, 100))

player_orange_right = pygame.image.load('Images/orange_right.png')
player_orange_right = pygame.transform.scale(player_orange_right, (100, 100))

player_blue_left = pygame.image.load('Images/blue_left.png')
player_blue_left = pygame.transform.scale(player_blue_left, (100, 100))

player_blue_right = pygame.image.load('Images/blue_right.png')
player_blue_right = pygame.transform.scale(player_blue_right, (100, 100))

bg_img = pygame.image.load('Images/stars_bg.jpg')
bg_img = pygame.transform.scale(bg_img, (screen_width, screen_height))

explosion = pygame.image.load('Images/explosion.png')
explosion = pygame.transform.scale(explosion, (250, 250))

brg_1 = pygame.image.load('Images/blue_right_green_1.png')
brg_1 = pygame.transform.scale(brg_1, (100, 100))

brg_2 = pygame.image.load('Images/blue_right_green_2.png')
brg_2 = pygame.transform.scale(brg_2, (100, 100))

blg_1 = pygame.image.load('Images/blue_left_green_1.png')
blg_1 = pygame.transform.scale(blg_1, (100, 100))

blg_2 = pygame.image.load('Images/blue_left_green_2.png')
blg_2 = pygame.transform.scale(blg_2, (100, 100))

org_1 = pygame.image.load('Images/orange_right_green_1.png')
org_1 = pygame.transform.scale(org_1, (100, 100))

org_2 = pygame.image.load('Images/orange_right_green_2.png')
org_2 = pygame.transform.scale(org_2, (100, 100))

olg_1 = pygame.image.load('Images/orange_left_green_1.png')
olg_1 = pygame.transform.scale(olg_1, (100, 100))

olg_2 = pygame.image.load('Images/orange_left_green_2.png')
olg_2 = pygame.transform.scale(olg_2, (100, 100))

beam = pygame.image.load('Images/beam2.png')
beam = pygame.transform.scale(beam, (45, 700))


class player():
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.width = 100
        self.height = 100
        self.vel = 7
        self.left = False
        self.right = False
        self.color = color
        self.eat = False
        self.won = False
        self.cooldown = 0
        self.powered = False
        player.k = 20
        player.g = 1
        self.up = False
        self.down = False

    def draw(self):
        self.size()
        self.move()
        # pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

        if self.left:
            if self.powered:
                if player.g == 1:
                    screen.blit(olg_1, (self.x, self.y))
                else:
                    screen.blit(olg_2, (self.x, self.y))

            else:
                screen.blit(player_orange_left, (self.x, self.y))

        else:
            if self.powered:
                if player.g == 1:
                    screen.blit(org_1, (self.x, self.y))

                else:
                    screen.blit(org_2, (self.x, self.y))

            else:
                screen.blit(player_orange_right, (self.x, self.y))

    def move(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] and self.y > 0:
            self.y -= self.vel
            self.up = True
            self.down = False
        if keys[pygame.K_s] and self.y < screen_height - self.height:
            self.y += self.vel
            self.up = False
            self.down = True
        if keys[pygame.K_a] and self.x > 0:
            self.x -= self.vel
            self.left = True
            self.right = False
            self.up = False
            self.down = False
        if keys[pygame.K_d] and self.x < screen_width - self.width:
            self.x += self.vel
            self.left = False
            self.right = True
            self.up = False
            self.down = False

    def size(self):
        if self.eat == False:
            self.width, self.height = 100, 100


class player2(player):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)

    def move(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and self.y > 0:
            self.y -= self.vel

        if keys[pygame.K_DOWN] and self.y < screen_height - self.height:
            self.y += self.vel
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.vel
            self.left = True
            self.right = False
        if keys[pygame.K_RIGHT] and self.x < screen_width - self.width:
            self.x += self.vel
            self.left = False
            self.right = True

    def draw(self):
        self.size()
        self.move()
        if self.left:
            if self.powered:
                if player.g == 1:
                    screen.blit(blg_1, (self.x, self.y))
                else:
                    screen.blit(blg_2, (self.x, self.y))

            else:
                screen.blit(player_blue_left, (self.x, self.y))

        else:
            if self.powered:
                if player.g == 1:
                    screen.blit(brg_1, (self.x, self.y))

                else:
                    screen.blit(brg_2, (self.x, self.y))

            else:
                screen.blit(player_blue_right, (self.x, self.y))


class projectile():
    bullets = []
    up = False
    down = False

    def __init__(self, x, y, facing, player):
        self.x = x
        self.y = y
        self.color = (0, 255, 0)
        self.radius = 10
        self.facing = facing
        self.vel = 20 * facing
        self.player = player
        self.width = 20
        self.height = 5

    def move(self):
        for b in projectile.bullets:
            if 1000 > b.x > 0:
                b.x += b.vel
            else:
                projectile.bullets.pop(projectile.bullets.index(b))

    def draw(self):

        self.move()
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))


class food():
    current_food = []

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (0, 0, 0)
        self.radius = 25

    def draw(self):
        screen.blit(food_img, (self.x, self.y))


class beams():
    life = 50
    current_beam = []
    is_beam = False

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        if box.powered:
            screen.blit(beam, (box.x + 2 + box.width / 4, box.y + 80))
        else:
            screen.blit(beam, (box2.x + 2 + box.width / 4, box2.y + 80))


box = player(0, 0, (255, 128, 0))
box2 = player2(screen_width - 100, screen_height - 100, (51, 51, 255))


def reset():
    box.x, box.y = 0, 0
    box2.x, box2.y = screen_width - 100, screen_height - 100
    projectile.bullets = []
    box.eat, box2.eat = False, False
    food.current_food = []
    box.cooldown, box2.cooldown = 0, 0

    if box2.won:
        score['box2'] += 1

        # screen.fill((51, 51, 255))


    else:
        score['box'] += 1

        # screen.fill((255, 128, 0))

    pygame.display.update()
    pygame.time.delay(1000)

    box.powered = False
    box2.powered = False

    box.won = False
    box2.won = False


def redraw():
    screen.blit(bg_img, (0, 0))

    for b in projectile.bullets:
        b.draw()

    for f in food.current_food:
        f.draw()

    box.draw()
    box2.draw()

    for b in beams.current_beam:
        b.draw()

    textsurface = myfont.render('Orange: ' + str(score['box']) + ' Blue: ' + str(score['box2']), False, (255, 255, 255))
    screen.blit(textsurface, (300, 0))

    pygame.display.update()

x = 0
while running:

    pygame.time.delay(15)

    if len(beams.current_beam) > 0:
        beams.life -= 1
        if beams.life == 0:
            beams.current_beam = []
            beams.life = 50
            box.powered = False
            box2.powered = False
            beams.is_beam = False

    if player.k == 10:
        player.g = 1

    if player.g == 1:
        player.k -= 1
        if player.k == -10:
            player.g = 2

    if player.g == 2:
        player.k += 1

    box.cooldown -= 1
    box2.cooldown -= 1

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if box.cooldown <= 0:
            if box.up:
                projectile.up = True
            elif box.down:
                projectile.down = True

            if box.left:
                facing = -1
            else:
                facing = 1

            if len(projectile.bullets) < 2:
                projectile.bullets.append(
                    projectile(round(box.x + box.width // 2), round(box.y + box.height // 2), facing, 1))
            box.cooldown = 60

    if keys[pygame.K_f]:
        if box.powered:
            beams.current_beam.append(beams(box.x, box.y))
            beams.is_beam = True
            box.eat = False

    if keys[pygame.K_PERIOD]:
        if box2.powered:
            beams.current_beam.append(beams(box2.x, box2.y))
            beams.is_beam = True
            box2.eat = False

    if keys[pygame.K_SLASH]:
        if box2.cooldown <= 0:
            if box2.left:
                facing = -1
            else:
                facing = 1

            if len(projectile.bullets) < 2:
                projectile.bullets.append(
                    projectile(round(box2.x + box2.width // 2), round(box2.y + box2.height // 2), facing, 2))
            box2.cooldown = 60

    for b in projectile.bullets:
        if b.x in range(box.x, box.x + box.width) and b.y in range(box.y, box.y + box.height):
            if b.player == 2:
                box2.won = True
                screen.blit(explosion, (box.x - 60, box.y - 70))
                reset()

        if b.x in range(box2.x, box2.x + box2.width) and b.y in range(box2.y, box2.y + box2.height):
            if b.player == 1:
                box.won = True
                screen.blit(explosion, (box2.x - 60, box2.y - 70))
                reset()

    if not box.eat and not box2.eat:
        x = random.randint(1, 500)

        if x == 1 and len(food.current_food) == 0:
            food.current_food.append(food(random.randint(0, screen_width - 64), random.randint(0, screen_height - 64)))

    for f in food.current_food:
        if f.x in range(box.x, box.x + box.width) and f.y in range(box.y, box.y + box.height):
            food.current_food = []
            box.powered = True
            box.eat = True

        if f.x in range(box2.x, box2.x + box2.width) and f.y in range(box2.y, box2.y + box2.height):
            food.current_food = []
            box2.powered = True
            box2.eat = True

    if beams.is_beam:
        if box.powered:
            if (box.x + 2 + box.width / 4) in range(box2.x, box2.x + 100) or ((box.x + 2 + box.width / 4) + 45) in range(box2.x, box2.x + 100):
                if box.y < box2.y:
                    box.won = True
                    screen.blit(explosion, (box2.x - 60, box2.y - 70))
                    screen.blit(beam, (box.x + 2 + box.width / 4, box.y + 80))
                    reset()
        if box2.powered:
            if (box2.x + 2 + box2.width / 4) in range(box.x, box.x + 100) or ((box2.x + 2 + box2.width / 4) + 45) in range(box.x, box.x + 100):
                if box2.y < box.y:
                    box2.won = True
                    screen.blit(explosion, (box.x - 60, box.y - 70))
                    screen.blit(beam, (box2.x + 2 + box2.width / 4, box2.y + 80))
                    reset()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    redraw()

pygame.quit()

print(x)