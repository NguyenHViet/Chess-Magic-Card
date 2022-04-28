import pygame
import random

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

class BoardEnv:
    """
    Lớp môi trường bàn cờ chứa đường dẫn tới địa chỉ hình ảnh
    """
    __TypeEnv = ['desert','snow_moutain','swamp','foggy_forest','wind_canyon']
    _enviroment = random.choice(__TypeEnv)
    _TypeCell = ['Normal','Special']

    def __init__(self, _enviroment, _TypeCell):
        self.image = 'img\\' + _enviroment + '\\' + random.choice(_TypeCell) + '.png'
        # Load hình ảnh bàn cờ
        self.board_order = {(0, 0): None, (1, 0): None,
                       (2, 0): None, (3, 0): None,
                       (4, 0): None, (5, 0): None,
                       (6, 0): None, (7, 0): None,

                       (0, 1): pygame.image.load(self.image), (1, 1): pygame.image.load(self.image),
                       (2, 1): pygame.image.load(self.image), (3, 1): pygame.image.load(self.image),
                       (4, 1): pygame.image.load(self.image), (5, 1): pygame.image.load(self.image),
                       (6, 1): pygame.image.load(self.image), (7, 1): pygame.image.load(self.image),
                       (0, 2): pygame.image.load(self.image), (1, 2): pygame.image.load(self.image),
                       (2, 2): pygame.image.load(self.image), (3, 2): pygame.image.load(self.image),
                       (4, 2): pygame.image.load(self.image), (5, 2): pygame.image.load(self.image),
                       (6, 2): pygame.image.load(self.image), (7, 2): pygame.image.load(self.image),
                       (0, 3): pygame.image.load(self.image), (1, 3): pygame.image.load(self.image),
                       (2, 3): pygame.image.load(self.image), (3, 3): pygame.image.load(self.image),
                       (4, 3): pygame.image.load(self.image), (5, 3): pygame.image.load(self.image),
                       (6, 3): pygame.image.load(self.image), (7, 3): pygame.image.load(self.image),
                       (0, 4): pygame.image.load(self.image), (1, 4): pygame.image.load(self.image),
                       (2, 4): pygame.image.load(self.image), (3, 4): pygame.image.load(self.image),
                       (4, 4): pygame.image.load(self.image), (5, 4): pygame.image.load(self.image),
                       (6, 4): pygame.image.load(self.image), (7, 4): pygame.image.load(self.image),
                       (0, 5): pygame.image.load(self.image), (1, 5): pygame.image.load(self.image),
                       (2, 5): pygame.image.load(self.image), (3, 5): pygame.image.load(self.image),
                       (4, 5): pygame.image.load(self.image), (5, 5): pygame.image.load(self.image),
                       (6, 5): pygame.image.load(self.image), (7, 5): pygame.image.load(self.image),
                       (0, 6): pygame.image.load(self.image), (1, 6): pygame.image.load(self.image),
                       (2, 6): pygame.image.load(self.image), (3, 6): pygame.image.load(self.image),
                       (4, 6): pygame.image.load(self.image), (5, 6): pygame.image.load(self.image),
                       (6, 6): pygame.image.load(self.image), (7, 6): pygame.image.load(self.image),

                       (0, 7): None, (1, 7): None,
                       (2, 7): None, (3, 7): None,
                       (4, 7): None, (5, 7): None,
                       (6, 7): None, (7, 7): None}


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
                  (6, 7): pygame.image.load(wkn.image), (7, 7): pygame.image.load(wr.image)}

# Khởi tạo đặc tính ô cờ

