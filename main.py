import pygame
import sys
import time
import init

pygame.init()

# Kích thước window
WinWidth = 1600
WinHeight = 1000
# Kích thước sàn đấu
WIDTH = 800
HEIGHT = 800
offsetWidth = (WinWidth - WIDTH)/2
offsetHeight = (WinHeight - HEIGHT)/2
WIN = pygame.display.set_mode((WinWidth, WinHeight))
WHITE = (255, 255, 255)
GREY = (128, 128, 128)
YELLOW = (204, 204, 0)
BLUE = (50, 255, 255)
BLACK = (0, 0, 0)
pygame.display.set_caption("Chess: Magic Card")
WIN.fill("white")

class Node:
    def __init__(self, row, col, width):
        self.row = row
        self.col = col
        self.x = offsetWidth + int(row * width)
        self.y = offsetHeight + int(col * width)
        self.colour = WHITE
        self.occupied = None

    def draw(self, WIN):
        """
        Vẽ hình vuông trên window
        """
        pygame.draw.rect(WIN, self.colour, (self.x, self.y, WIDTH / 8, WIDTH / 8))

    def setup(self, WIN):
        """
        In hình ảnh quân cờ lên window
        """
        if init.starting_order[(self.row, self.col)]:
            if init.starting_order[(self.row, self.col)] == None:
                pass
            else:
                WIN.blit(init.starting_order[(self.row, self.col)], (self.x + 20, 20 + self.y))


def make_grid(rows, width):
    """
    Tạo các ô trên bàn cờ
    """
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(j, i, gap)
            grid[i].append(node)
            if (i+j)%2 ==1:
                grid[i][j].colour = GREY
    return grid


def draw_grid(win, rows, width):
    """
    Kẻ các đường thẳng ngăn cách
    """
    gap = width // 8
    for i in range(rows + 1):
        pygame.draw.line(win, BLACK, (offsetWidth, offsetHeight + i * gap), (offsetWidth + width, offsetHeight + i * gap))
        for j in range(rows + 1):
            pygame.draw.line(win, BLACK, (offsetWidth + j * gap, offsetHeight), (offsetWidth + j * gap, offsetHeight + width))

def update_display(win, grid, rows, width, moves):
    """
    Cập nhập hiển thị
    """
    if moves%2:
        teamColor = BLACK
    else:
        teamColor = WHITE

    for row in grid:
        for spot in row:
            spot.draw(win)
            spot.setup(win)
    draw_grid(win, rows, width)
    pygame.draw.circle(win, teamColor, (100, 100), 100, 1)
    pygame.display.update()


def Find_Node(pos, WIDTH):
    """
    Tìm ô trên bàn cờ
    """
    interval = WIDTH / 8
    y, x = pos
    rows = (y - offsetWidth) // interval
    columns = (x - offsetHeight) // interval
    return int(rows), int(columns)


def display_potential_moves(positions, grid):
    """
    Chuyển sang màu xanh với các ô thuộc nước đi khả thi
    """
    for i in positions:
        x, y = i
        grid[x][y].colour = BLUE


def Do_Move(OriginalPos, FinalPosition, WIN):
    init.starting_order[FinalPosition] = init.starting_order[OriginalPos]
    init.starting_order[OriginalPos] = None


def remove_highlight(grid):
    """
    Chuyển đổi về màu ban đầu của bàn cờ
    """
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i+j)%2 == 0:
                grid[i][j].colour = WHITE
            else:
                grid[i][j].colour = GREY
    return grid

init.create_board(init.board)


def main(WIN, WIDTH):
    moves = 0
    selected = False
    piece_to_move=[]
    grid = make_grid(8, WIDTH)
    while True:
        pygame.time.delay(50) ##stops cpu dying
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            """This quits the program if the player closes the window"""

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                y, x = Find_Node(pos, WIDTH)
                if selected == False:
                    try:
                        possible = init.select_moves((init.board[x][y]), (x,y), moves)
                        display_potential_moves(possible, grid)
                        piece_to_move = x,y
                        selected = True
                    except:
                        piece_to_move = []
                        print('Can\'t select')
                    #print(piece_to_move)

                else:
                    try:
                        if init.board[x][y].killable == True:
                            row, col = piece_to_move ## coords of original piece
                            init.board[x][y] = init.board[row][col]
                            init.board[row][col] = '  '
                            init.deselect()
                            remove_highlight(grid)
                            Do_Move((col, row), (y, x), WIN)
                            moves += 1
                            print(init.convert_to_readable(init.board))
                        else:
                            init.deselect()
                            remove_highlight(grid)
                            selected = False
                            print("Deselected")
                    except:
                        if init.board[x][y] == 'x ':
                            row, col = piece_to_move
                            init.board[x][y] = init.board[row][col]
                            init.board[row][col] = '  '
                            init.deselect()
                            remove_highlight(grid)
                            Do_Move((col, row), (y, x), WIN)
                            moves += 1
                            print(init.convert_to_readable(init.board))
                        else:
                            init.deselect()
                            remove_highlight(grid)
                            selected = False
                            print("Invalid move")
                    selected = False

            update_display(WIN, grid, 8, WIDTH, moves)


main(WIN, WIDTH)