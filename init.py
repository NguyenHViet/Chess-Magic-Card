import pygame

board = [['  ' for i in range(8)] for i in range(8)]

class Piece:
    """
    Lớp quân cờ bao gồm các thuộc tính cơ bản:
    Đội, loại, địa chỉ hình ảnh, có thể bị giết hay không.
    Các thuộc tính thêm:
    Hiệu ứng (tốt hoặc xấu)
    """
    def __init__(self, team, type, image, killable = False):
        self.team = team
        self.type = type
        self.killable = killable
        self.image = image
        self.effect = []

# Khởi tạo quân chốt
bp = Piece('b', 'p', 'img\\b_pawn.png')
wp = Piece('w', 'p', 'img\w_pawn.png')
# Khởi tạo quân vua
bk = Piece('b', 'k', 'img\\b_king.png')
wk = Piece('w', 'k', 'img\w_king.png')
# Khởi tạo quân xe
br = Piece('b', 'r', 'img\\b_rook.png')
wr = Piece('w', 'r', 'img\w_rook.png')
# Khởi tạo quân tượng
bb = Piece('b', 'b', 'img\\b_bishop.png')
wb = Piece('w', 'b', 'img\w_bishop.png')
# Khởi tạo quân hậu
bq = Piece('b', 'q', 'img\\b_queen.png')
wq = Piece('w', 'q', 'img\w_queen.png')
# Khởi tạo quân mã
bkn = Piece('b', 'kn', 'img\\b_knight.png')
wkn = Piece('w', 'kn', 'img\w_knight.png')

# Load hình ảnh sẵn
starting_order = {(0, 0): pygame.image.load(br.image), (1, 0): pygame.image.load(bkn.image),
                  (2, 0): pygame.image.load(bb.image), (3, 0): pygame.image.load(bk.image),
                  (4, 0): pygame.image.load(bq.image), (5, 0): pygame.image.load(bb.image),
                  (6, 0): pygame.image.load(bkn.image), (7, 0): pygame.image.load(br.image),
                  (0, 1): pygame.image.load(bp.image), (1, 1): pygame.image.load(bp.image),
                  (2, 1): pygame.image.load(bp.image), (3, 1): pygame.image.load(bp.image),
                  (4, 1): pygame.image.load(bp.image), (5, 1): pygame.image.load(bp.image),
                  (6, 1): pygame.image.load(bp.image), (7, 1): pygame.image.load(bp.image),

                  (0, 2): None, (1, 2): None, (2, 2): None, (3, 2): None,
                  (4, 2): None, (5, 2): None, (6, 2): None, (7, 2): None,
                  (0, 3): None, (1, 3): None, (2, 3): None, (3, 3): None,
                  (4, 3): None, (5, 3): None, (6, 3): None, (7, 3): None,
                  (0, 4): None, (1, 4): None, (2, 4): None, (3, 4): None,
                  (4, 4): None, (5, 4): None, (6, 4): None, (7, 4): None,
                  (0, 5): None, (1, 5): None, (2, 5): None, (3, 5): None,
                  (4, 5): None, (5, 5): None, (6, 5): None, (7, 5): None,

                  (0, 6): pygame.image.load(wp.image), (1, 6): pygame.image.load(wp.image),
                  (2, 6): pygame.image.load(wp.image), (3, 6): pygame.image.load(wp.image),
                  (4, 6): pygame.image.load(wp.image), (5, 6): pygame.image.load(wp.image),
                  (6, 6): pygame.image.load(wp.image), (7, 6): pygame.image.load(wp.image),
                  (0, 7): pygame.image.load(wr.image), (1, 7): pygame.image.load(wkn.image),
                  (2, 7): pygame.image.load(wb.image), (3, 7): pygame.image.load(wk.image),
                  (4, 7): pygame.image.load(wq.image), (5, 7): pygame.image.load(wb.image),
                  (6, 7): pygame.image.load(wkn.image), (7, 7): pygame.image.load(wr.image),}

def create_board(board):
    """
    Khởi tạo bàn cờ cùng các quân cờ tại vị trí ban đầu
    """
    board[0] = [Piece('b', 'r', 'img\\b_rook.png'), Piece('b', 'kn', 'img\\b_knight.png'), Piece('b', 'b', 'img\\b_bishop.png'), \
               Piece('b', 'q', 'img\\b_queen.png'), Piece('b', 'k', 'img\\b_king.png'), Piece('b', 'b', 'img\\b_bishop.png'), \
               Piece('b', 'kn', 'img\\b_knight.png'), Piece('b', 'r', 'img\\b_rook.png')]

    board[7] = [Piece('w', 'r', 'img\w_rook.png'), Piece('w', 'kn', 'img\w_knight.png'), Piece('w', 'b', 'img\w_bishop.png'), \
               Piece('w', 'q', 'img\w_queen.png'), Piece('w', 'k', 'img\w_king.png'), Piece('w', 'b', 'img\w_bishop.png'), \
               Piece('w', 'kn', 'img\w_knight.png'), Piece('w', 'r', 'img\w_rook.png')]

    for i in range(8):
        board[1][i] = Piece('b', 'p', 'img\\b_pawn.png')
        board[6][i] = Piece('w', 'p', 'img\w_pawn.png')
    return board

def on_board(position):
    """
    Kiểm tra xem thử vị trí đầu vào có nằm trên bàn cờ không
    """
    if position[0] > -1 and position[1] > -1 and position[0] < 8 and position[1] < 8:
        return True

def convert_to_readable(board):
    """
    Chuyển bàn cờ về dạng đọc được
    """
    output = ''

    for i in board:
        for j in i:
            try:
                output += j.team + j.type + ', '
            except:
                output += j + ', '
        output += '\n'
    return output

def deselect():
    """
    Hủy lựa chọn quân cờ hiện tại
    """
    for row in range(len(board)):
        for column in range(len(board[0])):
            if board[row][column] == 'x ':
                board[row][column] = '  '
            else:
                try:
                    board[row][column].killable = False
                except:
                    pass
    return convert_to_readable(board)

def highlight(board):
    """
    Xuất ra danh sách các vị trí có nước đi đang khả thi trên bàn
    """
    highlighted = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'x ':
                highlighted.append((i, j))
            else:
                try:
                    if board[i][j].killable:
                        highlighted.append((i, j))
                except:
                    pass
    return highlighted

def check_team(moves, index):
    """
    Kiểm tra lượt đi
    """
    row, col = index
    if moves%2 == 0:
        if board[row][col].team == 'w':
            return True
    else:
        if board[row][col].team == 'b':
            return True

def select_moves(piece, index, moves):
    """
    Xuất danh sách các vị trí có nước đi khả thi tương ứng của quân cờ đang được chọn
    """
    if check_team(moves, index):
        if piece.type == 'p':
            if piece.team == 'b':
                return highlight(pawn_moves_b(index))
            else:
                return highlight(pawn_moves_w(index))

        if piece.type == 'k':
            return highlight(king_moves(index))

        if piece.type == 'r':
            return highlight(rook_moves(index))

        if piece.type == 'b':
            return highlight(bishop_moves(index))

        if piece.type == 'q':
            return highlight(queen_moves(index))

        if piece.type == 'kn':
            return highlight(knight_moves(index))

def pawn_moves_b(index):
    """
    Các phương thức di chuyển của quân chốt đen
    Input: index: vị trí hiện tại
    """
    if index[0] == 1:
        if board[index[0] + 2][index[1]] == '  ' and board[index[0] + 1][index[1]] == '  ':
            board[index[0] + 2][index[1]] = 'x '
    bottom3 = [[index[0] + 1, index[1] + i] for i in range(-1, 2)]

    for positions in bottom3:
        if on_board(positions):
            if bottom3.index(positions) % 2 == 0:
                try:
                    if board[positions[0]][positions[1]].team != 'b':
                        board[positions[0]][positions[1]].killable = True
                except:
                    pass
            else:
                if board[positions[0]][positions[1]] == '  ':
                    board[positions[0]][positions[1]] = 'x '
    return board

def pawn_moves_w(index):
    """
    Các phương thức di chuyển của quân chốt trắng
    Input: index: vị trí hiện tại
    """
    if index[0] == 6:
        if board[index[0] - 2][index[1]] == '  ' and board[index[0] - 1][index[1]] == '  ':
            board[index[0] - 2][index[1]] = 'x '
    top3 = [[index[0] - 1, index[1] + i] for i in range(-1, 2)]

    for positions in top3:
        if on_board(positions):
            if top3.index(positions) % 2 == 0:
                try:
                    if board[positions[0]][positions[1]].team != 'w':
                        board[positions[0]][positions[1]].killable = True
                except:
                    pass
            else:
                if board[positions[0]][positions[1]] == '  ':
                    board[positions[0]][positions[1]] = 'x '
    return board

def king_moves(index):
    """
    Các phương thức di chuyển của quân vua
    Input: index: vị trí hiện tại
    """
    for y in range(3):
        for x in range(3):
            if on_board((index[0] - 1 + y, index[1] - 1 + x)):
                if board[index[0] - 1 + y][index[1] - 1 + x] == '  ':
                    board[index[0] - 1 + y][index[1] - 1 + x] = 'x '
                else:
                    if board[index[0] - 1 + y][index[1] - 1 + x].team != board[index[0]][index[1]].team:
                        board[index[0] - 1 + y][index[1] - 1 + x].killable = True
    return board

def rook_moves(index):
    """
    Các phương thức di chuyển của quân xe
    Input: index: vị trí hiện tại
    """
    cross = [[[index[0] + i, index[1]] for i in range(1, 8 - index[0])],
             [[index[0] - i, index[1]] for i in range(1, index[0] + 1)],
             [[index[0], index[1] + i] for i in range(1, 8 - index[1])],
             [[index[0], index[1] - i] for i in range(1, index[1] + 1)]]

    for direction in cross:
        for positions in direction:
            if on_board(positions):
                if board[positions[0]][positions[1]] == '  ':
                    board[positions[0]][positions[1]] = 'x '
                else:
                    if board[positions[0]][positions[1]].team != board[index[0]][index[1]].team:
                        board[positions[0]][positions[1]].killable = True
                    break
    return board

def bishop_moves(index):
    """
    Các phương thức di chuyển của quân tượng
    Input: index: vị trí hiện tại
    """
    diagonals = [[[index[0] + i, index[1] + i] for i in range(1, 8)],
                 [[index[0] + i, index[1] - i] for i in range(1, 8)],
                 [[index[0] - i, index[1] + i] for i in range(1, 8)],
                 [[index[0] - i, index[1] - i] for i in range(1, 8)]]

    for direction in diagonals:
        for positions in direction:
            if on_board(positions):
                if board[positions[0]][positions[1]] == '  ':
                    board[positions[0]][positions[1]] = 'x '
                else:
                    if board[positions[0]][positions[1]].team != board[index[0]][index[1]].team:
                        board[positions[0]][positions[1]].killable = True
                    break
    return board

def queen_moves(index):
    """
    Các phương thức di chuyển của quân hậu
    Input: index: vị trí hiện tại
    """
    board = rook_moves(index)
    board = bishop_moves(index)
    return board

def knight_moves(index):
    """
    Các phương thức di chuyển của quân mã
    Input: index: vị trí hiện tại
    """
    for i in range(-2, 3):
        for j in range(-2, 3):
            if i ** 2 + j ** 2 == 5:
                if on_board((index[0] + i, index[1] + j)):
                    if board[index[0] + i][index[1] + j] == '  ':
                        board[index[0] + i][index[1] + j] = 'x '
                    else:
                        if board[index[0] + i][index[1] + j].team != board[index[0]][index[1]].team:
                            board[index[0] + i][index[1] + j].killable = True
    return board
