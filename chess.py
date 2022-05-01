import pygame
import effect as ef

PHASE = {
    'Start': 0, 'Picking': 1, 'Move': 2, 'Cast': 3, 'End': 4, 'Finish': 5
}


class Chess:
    """
    Lớp "Quân Cờ"
    """
    def __init__(self, team, typechess, direction, img, score = 0, effects = [], speed = 0):
        """
        Hàm khởi tạo quân cờ.
        :param team: Tên đội (str)
        :param typechess: Kiểu quân cờ (str)
        :param direction: Hướng di chuyển (str)
        :param img: Hình ảnh quân cờ (pygame.image)
        :param score: Điểm của quân cờ (int)
        :param effects: Danh sách hiệu ứng (list of str)
        """
        self._team = team
        self._type = typechess
        self._direction = direction
        self._image = img
        self._score = score
        self._effects = [ef.Effect('!')] + effects
        self._startSpeed = speed
        self._speed = self._startSpeed
        self._killable = False

    def get_effects(self):
        """
        Lấy danh sách hiệu ứng của quân cờ.
        :return: Danh sách hiệu ứng của quân cờ (List of str)
        """
        return self._effects

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

    def get_dir(self):
        return self._direction

    def get_killable(self):
        return self._killable

    def is_effective(self, effect = ""):
        """
        Trả về True nếu quân cờ có giá trị hiệu ứng đầu vào, ngược lại trả về False.
        :param effect: Hiệu ứng cần kiểm tra (str)
        :return: Giá trị boolen
        """
        return effect in self._effects

    def convert_to_readable(self):
        """
        Chuyển quân cờ thành dạng có thể đọc được
        :return: Chuỗi ký tự self.team + self.type
        """
        return str(self._team + self._type)

    def get_moves(self, oBoard, rBoard, index):
        """
        Xuất ra các cách di chuyển của quân cờ
        :param oBoard: Ma trận 2D các Object trên bàn cờ (2D list)
        :param rBoard: Ma trận 2D dạng str các object trên bàn cờ (2D list)
        :param index: Tạo độ quân cờ trên bàn cờ (tuple(row, col))
        """
        pass

    def draw(self, win, pos, width = 60):
        """
        Vẽ hình ảnh quân cờ trên cửa sổ
        :param win: Cửa sổ được chọn (pygame.display)
        :param pos: Vị trí hình ảnh được vẽ (tuple(x, y))
        """
        win.blit(pygame.transform.scale(self._image, (width, width)), pos)

    def set_killable(self, able):
        """
        Gán killable là True nếu quân cờ không có hiệu ứng "Imortal"
        """
        if not self.is_effective("Imortal") and able:
            self._killable = True
        else:
            self._killable = False

    def set_score(self, new_score):
        """
        Gán giá trị điểm mới cho quân cờ
        :param new_score: Điểm số mới (int)
        """
        self._score = new_score

    def change_speed(self, cspeed):
        self._speed += cspeed

    def add_effect(self, effect):
        """
        Tăng thêm hiệu ứng cho quân cờ
        :param effect: Hiệu ứng mới
        """
        self._effects += effect

    def delete_effect(self, effect):
        if effect in self._effects:
            self._effects.remove(effect)

    def active_effects(self, oBoard, rBoard, index, phase):
        for effect in self._effects:
            try:
                effect.active_effect(oBoard, rBoard, index, phase)
            except:
                pass

    def triggered_effects(self):
        for effect in self._effects:
            try:
                effect.triggered_effect()
            except:
                pass

    def update(self, oBoard, rBoard, index, phase):
        if phase == PHASE['End']:
            self._speed = self._startSpeed
        for effect in self._effects:
            try:
                if phase == PHASE['End']:
                    effect.unactive_effect()
                if effect.is_over():
                    self.delete_effect(effect)
                effect.active_effect(oBoard, rBoard, index, phase)
            except:
                pass

def on_board(index):
    """
    Kiểm tra xem thử vị trí đầu vào có nằm trên bàn cờ không
    :param index: Vị trí kiểm tra (tuple(x, y))
    """
    if index[0] > -1 and index[1] > -1 and index[0] < 8 and index[1] < 8:
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
        super().__init__(team, "pawn",direction, img, 10, [ef.Effect('IncreaseSpeed', turns = 1000, phase = 1)], 1)

    def get_moves(self, oBoard, rBoard, index):
        rBoard[index[0]][index[1]] += ':'
        direction = -1
        if self._direction == 'downward':
            direction = 1

        for i in range(1, self._speed + 1):
            if rBoard[index[0] + i * direction][index[1]] == ' ':
                rBoard[index[0] + i * direction][index[1]] = 'x'
            else:
                break
        top3 = [[index[0] + direction, index[1] + i] for i in range(-1, 2)]

        for positions in top3:
            if on_board(positions):
                if top3.index(positions) % 2 == 0:
                    try:
                        if oBoard[(positions[1], positions[0])].get_team() != self.get_team():
                            oBoard[(positions[1], positions[0])].set_killable(True)
                            rBoard[positions[0]][positions[1]] = 'x'
                    except:
                        pass
                else:
                    if rBoard[positions[0]][positions[1]] == ' ':
                        rBoard[positions[0]][positions[1]] = 'x'

class King(Chess):
    def __init__(self, team, direction, img, effects = []):
        """
        Khởi tạo quân "Vua"
        :param team: Tên đội (str)
        :param img: Hình ảnh quân cờ (pygame.image)
        :param effects: Danh sách hiệu ứng (list of str)
        """
        super().__init__(team, "king", direction, img, 1000, effects, 1)

    def get_moves(self, oBoard, rBoard, index):
        rBoard[index[0]][index[1]] += ':'
        for y in range(3):
            for x in range(3):
                if on_board((index[0] - 1 + y, index[1] - 1 + x)):
                    if rBoard[index[0] - 1 + y][index[1] - 1 + x] == ' ':
                        rBoard[index[0] - 1 + y][index[1] - 1 + x] = 'x'
                    else:
                        try:
                            if oBoard[(index[1] - 1 + x, index[0] - 1 + y)].get_team() != self.get_team():
                                oBoard[(index[1] - 1 + x, index[0] - 1 + y)].set_killable(True)
                                rBoard[index[0] - 1 + y][index[1] - 1 + x] = 'x'
                        except:
                            pass

class Rook(Chess):
    def __init__(self, team, direction, img, effects = []):
        """
        Khởi tạo quân "Xa"
        :param team: Tên đội (str)
        :param img: Hình ảnh quân cờ (pygame.image)
        :param effects: Danh sách hiệu ứng (list of str)
        """
        super().__init__(team, "rook", direction, img, 50, effects, 8)

    def get_moves(self, oBoard, rBoard, index):
        rBoard[index[0]][index[1]] += ':'
        cross = [[[index[0] + i, index[1]] for i in range(1, 8 - index[0])],
                 [[index[0] - i, index[1]] for i in range(1, index[0] + 1)],
                 [[index[0], index[1] + i] for i in range(1, 8 - index[1])],
                 [[index[0], index[1] - i] for i in range(1, index[1] + 1)]]

        for dir in cross:
            for pos in dir:
                if on_board(pos):
                    if rBoard[pos[0]][pos[1]] == ' ':
                        print(pos)
                        rBoard[pos[0]][pos[1]] = 'x'
                    else:
                        try:
                            if oBoard[(pos[1], pos[0])].get_team() != self.get_team():
                                oBoard[(pos[1], pos[0])].set_killable(True)
                                rBoard[pos[0]][pos[1]] = 'x'
                            if not self.is_effective('Unstoppable'):
                                break
                        except:
                            pass

class Bishop(Chess):
    def __init__(self, team, direction, img, effects = []):
        """
        Khởi tạo quân "Tượng"
        :param team: Tên đội (str)
        :param img: Hình ảnh quân cờ (pygame.image)
        :param effects: Danh sách hiệu ứng (list of str)
        """
        super().__init__(team, "bishop", direction, img, 30, effects, 8)

    def get_moves(self, oBoard, rBoard, index):
        rBoard[index[0]][index[1]] += ':'
        diagonals = [[[index[0] + i, index[1] + i] for i in range(1, 8)],
                     [[index[0] + i, index[1] - i] for i in range(1, 8)],
                     [[index[0] - i, index[1] + i] for i in range(1, 8)],
                     [[index[0] - i, index[1] - i] for i in range(1, 8)]]

        for dir in diagonals:
            print(dir)
            for pos in dir:
                print(pos)
                if on_board(pos):
                    if rBoard[pos[0]][pos[1]] == ' ':
                        rBoard[pos[0]][pos[1]] = 'x'
                    else:
                        try:
                            if oBoard[(pos[1], pos[0])].get_team() != self.get_team():
                                oBoard[(pos[1], pos[0])].set_killable(True)
                                rBoard[pos[0]][pos[1]] = 'x'
                            if not self.is_effective('Unstoppable'):
                                break
                        except:
                            pass

class Knight(Chess):
    def __init__(self, team, direction, img, effects = []):
        """
        Khởi tạo quân "Mã"
        :param team: Tên đội (str)
        :param img: Hình ảnh quân cờ (pygame.image)
        :param effects: Danh sách hiệu ứng (list of str)
        """
        super().__init__(team, "knight", direction, img, 30, effects, 3)

    def get_moves(self, oBoard, rBoard, index):
        rBoard[index[0]][index[1]] += ':'
        for i in range(-2, 3):
            for j in range(-2, 3):
                if i ** 2 + j ** 2 == 5:
                    if on_board((index[0] + i, index[1] + j)):
                        if rBoard[index[0] + i][index[1] + j] == ' ':
                            rBoard[index[0] + i][index[1] + j] = 'x'
                        else:
                            try:
                                if oBoard[(index[1] + j, index[0] + i)].get_team() != self.get_team():
                                    oBoard[(index[1] + j, index[0] + i)].set_killable(True)
                                    rBoard[index[0] + i][index[1] + j] = 'x'
                            except:
                                pass

class Queen(Chess):
    def __init__(self, team, direction, img, effects = []):
        """
        Khởi tạo quân "Hậu"
        :param team: Tên đội (str)
        :param img: Hình ảnh quân cờ (pygame.image)
        :param effects: Danh sách hiệu ứng (list of str)
        """
        super().__init__(team, "queen", direction, img, 90, effects)

    def get_moves(self, oBoard, rBoard, index):
        rBoard[index[0]][index[1]] += ':'
        cross = [[[index[0] + i, index[1]] for i in range(1, 8 - index[0])],
                 [[index[0] - i, index[1]] for i in range(1, index[0] + 1)],
                 [[index[0], index[1] + i] for i in range(1, 8 - index[1])],
                 [[index[0], index[1] - i] for i in range(1, index[1] + 1)]]

        for dir in cross:
            for pos in dir:
                if on_board(pos):
                    if rBoard[pos[0]][pos[1]] == ' ':
                        rBoard[pos[0]][pos[1]] = 'x'
                    else:
                        try:
                            if oBoard[(pos[1], pos[0])].get_team() != self.get_team():
                                oBoard[(pos[1], pos[0])].set_killable(True)
                                rBoard[pos[0]][pos[1]] = 'x'
                            if not self.is_effective('Unstoppable'):
                                break
                        except:
                            pass

        diagonals = [[[index[0] + i, index[1] + i] for i in range(1, 8)],
                     [[index[0] + i, index[1] - i] for i in range(1, 8)],
                     [[index[0] - i, index[1] + i] for i in range(1, 8)],
                     [[index[0] - i, index[1] - i] for i in range(1, 8)]]

        diagonals = [[[index[0] + i, index[1] + i] for i in range(1, 8)],
                     [[index[0] + i, index[1] - i] for i in range(1, 8)],
                     [[index[0] - i, index[1] + i] for i in range(1, 8)],
                     [[index[0] - i, index[1] - i] for i in range(1, 8)]]

        for dir in diagonals:
            for pos in dir:
                if on_board(pos):
                    if rBoard[pos[0]][pos[1]] == ' ':
                        rBoard[pos[0]][pos[1]] = 'x'
                    else:
                        try:
                            if oBoard[(pos[1], pos[0])].get_team() != self.get_team():
                                oBoard[(pos[1], pos[0])].set_killable(True)
                                rBoard[pos[0]][pos[1]] = 'x'
                            if not self.is_effective('Unstoppable'):
                                break
                        except:
                            pass