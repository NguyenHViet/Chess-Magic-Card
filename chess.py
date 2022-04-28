import pygame

class Chess:
    """
    Lớp "Quân Cờ"
    """
    def __init__(self, team, typechess, img, score = 0, effects = []):
        """
        Hàm khởi tạo quân cờ.
        :param team: Tên đội (str)
        :param typechess: Kiểu quân cờ (str)
        :param score: Điểm của quân cờ (int)
        :param img: Hình ảnh quân cờ (pygame.image)
        :param effects: Danh sách hiệu ứng (list of str)
        """
        self._team = team
        self._type = typechess
        self._image = img
        self._score = score
        self._effects = []
        self._killable = False

    def get_effects(self):
        """
        Lấy danh sách hiệu ứng của quân cờ.
        :return: Danh sách hiệu ứng của quân cờ (List of str)
        """
        return self.effects

    def get_team(self):
        """
        Lấy tên đội của quân cờ
        :return: Tên đội (str)
        """
        return self._team

    def get_score(self):
        """
        Lấy điểm số của quân cờ
        :return: Điểm (int)
        """
        return self._score

    def is_effective(self, effect = ""):
        """
        Trả về True nếu quân cờ có giá trị hiệu ứng đầu vào, ngược lại trả về False.
        :param effect: Hiệu ứng cần kiểm tra (str)
        :return: Giá trị boolen
        """
        if effect in self.effects:
            return True
        else:
            return False

    def convert_to_readable(self):
        """
        Chuyển quân cờ thành dạng có thể đọc được
        :return: Chuỗi ký tự self.team + self.type
        """
        return str(self.team + self.type)

    def get_moves(self, board, index):
        """
        Xuất ra các cách di chuyển của quân cờ
        :param board: Ma trận 2D các Node trên bàn cờ (2D list)
        :param index: Tạo độ quân cờ trên bàn cờ (tuple(row, col))
        """
        pass

    def draw(self, win, pos):
        """
        Vẽ hình ảnh quân cờ trên cửa sổ
        :param win: Cửa sổ được chọn (pygame.display)
        :param pos: Vị trí hình ảnh được vẽ (tuple(x, y))
        """
        win.blit(self.image, pos)

    def set_killable(self):
        """
        Gán killable là True nếu quân cờ không có hiệu ứng "Imortal"
        """
        if not self.is_effective("Imortal"):
            self.killable = True

    def set_score(self, new_score):
        """
        Gán giá trị điểm mới cho quân cờ
        :param new_score: Điểm số mới (int)
        """
        self._score = new_score

    def add_effect(self, effect):
        """
        Tăng thêm hiệu ứng cho quân cờ
        :param effect: Hiệu ứng mới
        """
        self._effects += [effect]

def on_board(index):
    """
    Kiểm tra xem thử vị trí đầu vào có nằm trên bàn cờ không
    :param index: Vị trí kiểm tra (tuple(x, y))
    """
    if pos[0] > -1 and pos[1] > -1 and pos[0] < 8 and pos[1] < 8:
        return True

class Pawn(Chess):
    """
    Quân "Chốt"
    """
    def __init__(self, team, direction, img, effects = []):
        """
        Khởi tạo quân "Chốt"
        :param team: Tên đội (str)
        :param direction: Hướng di chuyển (str)
        :param img: Hình ảnh quân cờ (pygame.image)
        :param effects: Danh sách hiệu ứng (list of str)
        """
        super().__init__(team, "pawn", img, 10, effects)
        self.__fisrtMove = True
        self.__direction = direction

    def get_moves(self, board, index):
        if self._direction == "downward":
            direction = 1
        else:
            direction = -1
        pass

class King(Chess):
    def __init__(self, team, img, effects = []):
        """
        Khởi tạo quân "Vua"
        :param team: Tên đội (str)
        :param img: Hình ảnh quân cờ (pygame.image)
        :param effects: Danh sách hiệu ứng (list of str)
        """
        super().__init__(team, "king", direction, img, 1000, effects)

    def get_moves(self, board, index):
        pass

class Rook(Chess):
    def __init__(self, team, img, effects = []):
        """
        Khởi tạo quân "Xa"
        :param team: Tên đội (str)
        :param img: Hình ảnh quân cờ (pygame.image)
        :param effects: Danh sách hiệu ứng (list of str)
        """
        super().__init__(team, "rook", direction, img, 50, effects)

    def get_moves(self, board, index):
        pass

class Bishop(Chess):
    def __init__(self, team, img, effects = []):
        """
        Khởi tạo quân "Tượng"
        :param team: Tên đội (str)
        :param img: Hình ảnh quân cờ (pygame.image)
        :param effects: Danh sách hiệu ứng (list of str)
        """
        super().__init__(team, "bishop", direction, img, 30, effects)

    def get_moves(self, board, index):
        pass

class Knight(Chess):
    def __init__(self, team, img, effects = []):
        """
        Khởi tạo quân "Mã"
        :param team: Tên đội (str)
        :param img: Hình ảnh quân cờ (pygame.image)
        :param effects: Danh sách hiệu ứng (list of str)
        """
        super().__init__(team, "knight", direction, img, 30, effects)

    def get_moves(self, board, index):
        pass

class Queen(Chess):
    def __init__(self, team, img, effects = []):
        """
        Khởi tạo quân "Hậu"
        :param team: Tên đội (str)
        :param img: Hình ảnh quân cờ (pygame.image)
        :param effects: Danh sách hiệu ứng (list of str)
        """
        super().__init__(team, "queen", direction, img, 90, effects)

    def get_moves(self, board, index):
        pass