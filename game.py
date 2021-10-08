import pygame
import random
import copy

BLANK_BOARD = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
TEST_BOARD = [[2, 4, 8, 16], [32, 64, 128, 256], [512, 1024, 2048, 4096], [0, 0, 0, 0]]
WIDTH = 100
HEIGHT = 100


class Game:
    def __init__(self, board):
        self.board = copy.deepcopy(board)
        self.prev = copy.deepcopy(board)
        self.count = 0

    def move_left(self):
        merged = [[False, False, False, False], [False, False, False, False], [False, False, False, False],
                  [False, False, False, False]]
        self.prev = copy.deepcopy(self.board)
        y = 0
        success = False
        while y < 4:
            x = 1
            while x < 4:
                if self.board[x][y] != 0:
                    i = x
                    while i > 0:
                        if self.board[i][y] == self.board[i - 1][y] and merged[i - 1][y] == False:
                            self.board[i - 1][y] += self.board[i - 1][y]
                            self.board[i][y] = 0
                            i -= 1
                            success = True
                            self.count -= 1
                            merged[i][y] = True
                            break
                        else:
                            if self.board[i - 1][y] == 0:
                                self.board[i - 1][y] = self.board[i][y]
                                self.board[i][y] = 0
                                i -= 1
                                success = True
                            else:
                                break
                x += 1
            y += 1
        return success

    def move_right(self):
        merged = [[False, False, False, False], [False, False, False, False], [False, False, False, False],
                  [False, False, False, False]]
        self.prev = copy.deepcopy(self.board)
        y = 0
        success = False
        while y < 4:
            x = 2
            while x >= 0:
                if self.board[x][y] != 0:
                    i = x
                    while i < 3:
                        if self.board[i][y] == self.board[i + 1][y] and merged[i + 1][y] == False:
                            self.board[i + 1][y] += self.board[i][y]
                            self.board[i][y] = 0
                            i += 1
                            success = True
                            self.count -= 1
                            merged[i][y] = True
                            break
                        else:
                            if self.board[i + 1][y] == 0:
                                self.board[i + 1][y] = self.board[i][y]
                                self.board[i][y] = 0
                                i += 1
                                success = True
                            else:
                                break
                x -= 1
            y += 1
        return success

    def move_up(self):
        merged = [[False, False, False, False], [False, False, False, False], [False, False, False, False],
                  [False, False, False, False]]
        self.prev = copy.deepcopy(self.board)
        x = 0
        success = False
        while x < 4:
            y = 1
            while y < 4:
                if self.board[x][y] != 0:
                    i = y
                    while i > 0:
                        if self.board[x][i] == self.board[x][i - 1] and merged[x][i - 1] == False:
                            self.board[x][i - 1] += self.board[x][i]
                            self.board[x][i] = 0
                            i -= 1
                            success = True
                            self.count -= 1
                            merged[x][i] = True
                            break
                        else:
                            if self.board[x][i - 1] == 0:
                                self.board[x][i - 1] = self.board[x][i]
                                self.board[x][i] = 0
                                i -= 1
                                success = True
                            else:
                                break
                y += 1
            x += 1
        return success

    def move_down(self):
        merged = [[False, False, False, False], [False, False, False, False], [False, False, False, False],
                  [False, False, False, False]]
        self.prev = copy.deepcopy(self.board)
        x = 0
        success = False
        while x < 4:
            y = 2
            while y >= 0:
                if self.board[x][y] != 0:
                    i = y
                    while i < 3:
                        if self.board[x][i] == self.board[x][i + 1] and merged[x][i + 1] == False:
                            self.board[x][i + 1] += self.board[x][i]
                            self.board[x][i] = 0
                            i += 1
                            success = True
                            merged[x][i] = True
                            self.count -= 1
                            break
                        else:
                            if self.board[x][i + 1] == 0:
                                self.board[x][i + 1] = self.board[x][i]
                                self.board[x][i] = 0
                                i += 1
                                success = True
                            else:
                                break
                y -= 1
            x += 1
        return success

    def new(self):
        spaces = 16 - self.count
        j = random.randint(1, spaces)
        k = random.randint(1, 10)
        i = 1
        y = 0
        print('new')
        while y < 4:
            x = 0
            while x < 4:
                if self.board[x][y] == 0:
                    if i == j:
                        if k == 10:
                            self.board[x][y] = 4
                            self.count += 1
                            return
                        else:
                            self.count += 1
                            self.board[x][y] = 2
                            return
                    else:
                        i += 1
                x += 1
            y += 1

    def move(self, i):  # [left, right, up, down]
        if i == 0:
            if self.move_left() == True:
                self.new()
        if i == 1:
            if self.move_right() == True:
                self.new()
        if i == 2:
            if self.move_up() == True:
                self.new()
        if i == 3:
            if self.move_down() == True:
                self.new()

    def revert(self):
        self.board = copy.deepcopy(self.prev)


def game_over(board):
    test_game = Game(board)
    if test_game.count < 16:
        return False
    if test_game.move_down == True:
        test_game.revert()
        return False
    if test_game.move_up == True:
        test_game.revert()
        return False
    if test_game.move_left == True:
        test_game.revert()
        return False
    if test_game.move_right == True:
        test_game.revert()
        return False
    return True


def getColor(num):
    if num == 0:
        return (238, 255, 255)
    if num == 2:
        return (238, 228, 218)
    if num == 4:
        return (237, 224, 200)
    if num == 8:
        return (242, 177, 121)
    if num == 16:
        return (245, 149, 99)
    if num == 32:
        return (246, 124, 95)
    if num == 64:
        return (246, 94, 59)
    if num == 128:
        return (237, 207, 114)
    if num == 256:
        return (237, 204, 97)
    if num == 512:
        return (237, 200, 80)
    if num == 1024:
        return (237, 197, 63)
    if num == 2048:
        return (237, 194, 46)
    if num == 4096:
        return (237, 194, 255)
    else:
        return (255, 0, 0)

def draw_game(win, board):
    myfont = pygame.font.SysFont('Comic Sans MS', 22)
    win.fill((0, 0, 0))
    y = 0
    y_c = 40
    while y < 4:
        x = 0
        x_c = 40
        while x < 4:
            number = board[x][y]
            pygame.draw.rect(win, getColor(number), (x_c, y_c, WIDTH, HEIGHT))
            if number != 0:
                text = myfont.render(str(number), False, (0, 0, 0))
                textsurface = text.get_rect()
                textsurface.center = (x_c + ((WIDTH) // 2), y_c + ((HEIGHT) // 2))
                win.blit(text, textsurface)
            x += 1
            x_c += WIDTH + 4
        y += 1
        y_c += HEIGHT + 4
    pygame.display.update()


def main():
    pygame.init()
    win = pygame.display.set_mode((500, 500))
    pygame.display.list_modes()
    pygame.display.set_caption("2048")
    my_game = Game(BLANK_BOARD)
    my_game.new()
    my_game.new()
    run = True
    while run:
        draw_game(win, my_game.board)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT]:
                    my_game.move(0)
                if keys[pygame.K_RIGHT]:
                    print("move")
                    my_game.move(1)
                if keys[pygame.K_UP]:
                    my_game.move(2)
                if keys[pygame.K_DOWN]:
                    my_game.move(3)
                if keys[pygame.K_SPACE]:
                    my_game.revert()


main()
