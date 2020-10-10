import random
import pygame
import sys
pygame.font.init()

# global variables
WIDTH = 24
HEIGHT = 24
SIZE = 20
SCREEN_WIDTH = WIDTH * SIZE
SCREEN_HEIGHT = HEIGHT * SIZE
APPLE = False

DIR = {
    'u' : (0, -1), # north is -y
    'd' : (0, 1),
    'l' : (-1,0),
    'r' : (1,0)
}


class Snake(object):
    l = 1
    body = [(WIDTH // 2 + 1, HEIGHT // 2), (WIDTH // 2, HEIGHT // 2)]
    direction = 'r'
    dead = False

    def __init__(self):
        pass
    
    def get_color(self, i):
        hc = (40,50,100)
        tc = (90,130,255)
        return tuple(map(lambda x,y: (x * (self.l - i) + y * i ) / self.l, hc, tc))

    def get_head(self):
        return self.body[0]

    def turn(self, dir):
        # TODO: See section 3, "Turning the snake".
        self.direction = dir

    def collision(self, x, y):
        # TODO: See section 2, "Collisions", and section 4, "Self Collisions"
        for i in range(1, len(self.body)):
            # print(x, y)
            # print(self.body[i])
            if x == self.body[i][0] and y == self.body[i][1]:
                return True

        if x > 23 or x < 0 or y > 23 or y < 0:
            return True
        else:
            return False

    
    def coyote_time(self):
        # TODO: See section 13, "coyote time".
        pass

    def move(self):
        # TODO: See section 1, "Move the snake!". You will be revisiting this section a few times.
        global APPLE
        increment = DIR[self.direction]
        increment_x = increment[0]
        increment_y = increment[1]
        head_x = self.body[0][0]
        head_y = self.body[0][1]
        if self.collision(head_x + increment_x, head_y + increment_y):
            self.kill()
        head_x += increment_x
        head_y += increment_y
        prev = self.body[0]
        self.body[0] = (head_x, head_y)
        for i in range(1, len(self.body)):
            curr = self.body[i]
            self.body[i] = prev
            prev = curr
            if APPLE:
                print("Appending since apple")
                self.l += 1
                self.body.append(prev)
                APPLE = False

    def kill(self):
        # TODO: See section 11, "Try again!"
        self.dead = True

    def draw(self, surface):
        for i in range(len(self.body)):
            p = self.body[i]
            pos = (p[0] * SIZE, p[1] * SIZE)
            r = pygame.Rect(pos, (SIZE, SIZE))
            pygame.draw.rect(surface, self.get_color(i), r)

    def handle_keypress(self, k):
        if k == pygame.K_UP:
            self.turn('u')
        if k == pygame.K_DOWN:
            self.turn('d')
        if k == pygame.K_LEFT:
            self.turn('l')
        if k == pygame.K_RIGHT:
            self.turn('r')
    
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type != pygame.KEYDOWN:
                continue
            self.handle_keypress(event.key)
    
    def wait_for_key(self):
        # TODO: see section 10, "wait for user input".
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    return

# returns an integer between 0 and n, inclusive.
def rand_int(n):
    return random.randint(0, n)

class Apple(object):
    position = [10,10]
    color = (233, 70, 29)
    def __init__(self):
        self.place([])

    def place(self, snake):
        # TODO: see section 6, "moving the apple".
        pass

    def draw(self, surface):
        pos = (self.position[0] * SIZE, self.position[1] * SIZE)
        r = pygame.Rect(pos, (SIZE, SIZE))
        pygame.draw.rect(surface, self.color, r)

def draw_grid(surface):
    for y in range(0, HEIGHT):
        for x in range(0, WIDTH):
            r = pygame.Rect((x * SIZE, y * SIZE), (SIZE, SIZE))
            color = (169,215,81) if (x+y) % 2 == 0 else (162,208,73)
            pygame.draw.rect(surface, color, r)


def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    draw_grid(surface)
    snake = Snake()
    apple = Apple()
    snake.draw(surface)
    apple.draw(surface)
    screen.blit(surface, (0, 0))
    myfont = pygame.font.SysFont('agencyfb', 30)
    textsurface = myfont.render("Press Any Key to Start", False, (0, 0, 0))
    screen.blit(textsurface, (1, 1))
    pygame.display.update()

    score = 0
    speed = 5
    snake.wait_for_key()

    while True:
        # TODO: see section 9, "incremental difficulty".
        clock.tick(speed)
        snake.check_events()
        draw_grid(surface)        
        snake.move()

        snake.draw(surface)
        apple.draw(surface)

        # TODO: see section 5, "Eating the Apple".
        if Apple.position[0] == snake.body[0][0] and Apple.position[1] == snake.body[0][1]:
            speed += 1 # Implements Section 9
            print("Eating the Apple")
            score += 1
            global APPLE
            APPLE = True
            if random.randint(0, 1) == 1:
                Apple.position[0] = random.randint(0, snake.body[0][0])
            else:
                Apple.position[0] = random.randint(snake.body[-1][0], 23)
            if random.randint(0, 1) == 1:
                Apple.position[1] = random.randint(0, snake.body[0][1])
            else:
                Apple.position[1] = random.randint(snake.body[-1][1], 23)

        screen.blit(surface, (0,0))
        # TODO: see section 8, "Display the Score"
        textsurface = myfont.render("Score: " + str(score), False, (0, 0, 0))
        screen.blit(textsurface, (1, 1))
        pygame.display.update()
        if snake.dead:
            print('You died. Score: %d' % score)
            pygame.quit()
            sys.exit(0)

if __name__ == "__main__":
    main()