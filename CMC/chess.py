import copy

import pygame
import CMC.effect as ef

PHASE = {
    'Start': 0, 'Picking': 1, 'Move': 2, 'Cast': 3, 'End': 4, 'Finish': 5
}

'''
Các giai đoạn trong lượt
0: Đầu lượt đi
1: Suy Nghĩ
2: Chơi cờ
3: Chơi bài
4: Kết thúc lượt
5: Kết thúc trận
'''

class Chess:
    """
    Lớp "Quân Cờ"
    """
    def __init__(self, team = '', typechess = '', direction = '', img = '', score = 0, effects = [], speed = 0):
        """
        Hàm khởi tạo quân cờ.
        :param team: Tên đội (str)
        :param typechess: Kiểu quân cờ (str)
        :param direction: Hướng di chuyển (str)
        :param img: Hình ảnh quân cờ (pygame.image)
        :param score: Điểm của quân cờ (int)
        :param effects: Danh sách hiệu ứng (list(effect.Effect))
        :param speed: Tốc dộ di chuyển (int)
        """
        self._team = team
        self._type = typechess
        self._direction = direction
        self._image = img
        self._score = score
        self._effects = [] + effects
        self._startSpeed = speed
        self._speed = self._startSpeed
        self._killable = False
        self._MoveableCell = []

    def duplication(self):
        """
        Tạo bản sao quân cờ
        :return: bản sao quân cờ (chess.Chess)
        """
        dup_chess1 = copy.copy(self)
        dup_chess1.set_img('')
        dup_chess2 = copy.deepcopy(dup_chess1)
        return dup_chess2

    def get_effects(self):
        """
        Lấy danh sách hiệu ứng của quân cờ.
        :return: Danh sách hiệu ứng (list(effect.Effect))
        """
        return self._effects

    def get_team(self):
        """
        Lấy tên đội của quân cờ
        :return: Tên đội của quân cờ (str)
        """
        return self._team

    def get_type(self):
        """
        Lấy loại quân cờ
        :return: Loại quân cờ (str)
        """
        return self._type

    def get_score(self):
        """
        Lấy điểm số của quân cờ
        :return: Điểm của quân cờ (int)
        """
        return self._score

    def get_killable(self):
        """
        Kiểm tra xem có thể bị giết không
        :return: Thuộc tính killable của quân cờ (bool)
        """
        return self._killable

    def is_effective(self, effect = ""):
        """
        Trả về True nếu quân cờ có tên giống giá trị hiệu ứng đầu vào, ngược lại trả về False.
        :param effect: Tên hiệu ứng cần kiểm tra (str)
        :return: Giá trị đúng sai (bool)
        """
        return effect in [self.get_effects()[i].get_name() for i in range(len(self.get_effects()))]

    def convert_to_readable(self):
        """
        Chuyển quân cờ thành dạng có thể đọc được
        :return: Chuỗi bao gồm đội và loại quân cờ (str)
        """
        return str(self._team + self._type)

    def get_moves(self, nBoard, index, phase, mark='x', killable=True):
        """
        Đánh dấu các nước có thể di chuyển của quân cờ
        :param nBoard: Bàn cờ (board.Board)
        :param index: Tạo độ quân cờ trên bàn cờ (tuple(int, int))
        :param mark: Kí hiệu dùng để đánh dấu (str)
        :param phase: Giai đoạn của lượt hiện tại (int)
        :param killable: Giá trị được gán cho thuộc tính killable của quân cờ (bool)
        :return None
        """
        pass

    def get_direction(self):
        """
        Lấy hướng đi của quân cờ dưới dạng số
        :return: Hướng di chuyển (int)
        """
        direction = -1
        if self._direction == 'downward':
            direction = 1
        return direction

    def draw(self, win, pos, width = 60):
        """
        Vẽ hình ảnh quân cờ trên cửa sổ hiển thị
        :param win: Cửa sổ hiển thị được chọn (pygame.display)
        :param pos: Vị trí hình ảnh được vẽ (tuple(int, int))
        :return None
        """
        try:
            offsetHeight = (width - self._image.get_height()) / 2
            offsetWidth = (width - self._image.get_width()) / 2
            win.blit(self._image, (pos[0] + offsetHeight, pos[1] + offsetWidth))
        except:
            pass

    def set_img(self, new_img):
        """
        Gán hình ảnh mới
        :param new_img: hình ảnh mới (pygame.image)
        :return: None
        """
        self._image = new_img

    def set_killable(self, nBoard, index, phase, able):
        """
        Gán giá trị able cho thuộc tính killable
        :param nBoard: Bàn cờ (board.Board)
        :param index: Vị trí quân cờ (tuple(int, int))
        :param phase: Giai đoạn lượt hiện tại (int)
        :param able: Giá trị gán (bool)
        :return: None
        """
        if 'Fail' not in self.active_effects(nBoard, index, phase):
            self._killable = able

    def set_score(self, new_score):
        """
        Gán giá trị điểm mới cho quân cờ
        :param new_score: Điểm số mới (int)
        :return None
        """
        self._score = new_score

    def change_speed(self, cspeed):
        """
        Tăng tốc độ mới cho quân cờ
        :param cspeed: Lượng tốc độ được tăng (int)
        :return None
        """
        self._speed += cspeed

    def add_effect(self, effect = []):
        """
        Tăng thêm hiệu ứng cho quân cờ
        :param effect: Hiệu ứng mới (effect.Effect)
        :return None
        """
        self._effects += [effect]

    def delete_effect(self, effect):
        """
        Xóa hiệu ứng của quân cờ
        :param effect: Hiệu ứng cần xóa (effect.Effect)
        :return None
        """
        if effect in self._effects:
            self._effects.remove(effect)

    def active_effects(self, nBoard, index, phase):
        """
        Kích hoạt hiệu ứng của quân cờ
        :param nBoard: Bàn cờ (board.Board)
        :param index: Vị trí quân cờ (turple(int, int))
        :param phase: Giai đoạn của lượt đấu (int)
        :return None
        """
        result = []
        for effect in self._effects:
            try:
                result.append(effect.active_effect(nBoard, [index], phase))
            except:
                pass
        # if ef.STATUS[3] in result:
        #     print(self.convert_to_readable(), index)
        return result

    def unactive_effects(self):
        """
        Ngắt kích hoạt hiệu ứng của quân cờ
        :return: None
        """
        for effect in self._effects:
            try:
                effect.unactive_effect()
            except:
                pass

    def triggered_effects(self):
        """
        Giảm cộng dồn được tích trữ của các hiệu ứng của quân cờ
        :return None
        """
        for effect in self._effects:
            try:
                effect.triggered_effect()
            except:
                pass

    def update(self, nBoard, index, phase):
        """
        Cập nhập lại hiệu ứng của quân cờ
        :param nBoard: Bàn cờ (board.Board)
        :param index: Vị trí quân cờ (tuple(int, int))
        :param phase: Giai đoạn lượt đấu (int)
        :return Kết quả kích hoạt hiện ứng (list(str))
        """
        self._speed = self._startSpeed
        result = []
        for effect in self._effects:
            try:
                effect.unactive_effect()
                if effect.is_over(phase):
                    self.delete_effect(effect)
                result.append(effect.active_effect(nBoard, index, phase))
            except:
                pass
        return result

def on_board(index):
    """
    Kiểm tra xem thử vị trí đầu vào có nằm trên bàn cờ không
    :param index: Vị trí kiểm tra (tuple(int, int))
    :return Kết quả đúng sai (bool)
    """
    if index[0] > -1 and index[1] > -1 and index[0] < 8 and index[1] < 8:
        return True
    else:
        return False

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
        :param effects: Danh sách hiệu ứng (list(effect.Effect)
        """
        super().__init__(team, "Pawn", direction, img, 10, [ef.Effect('IncreaseSpeed', turns = -1, phase = 2)] + effects, 1)

    def get_moves(self, nBoard, index, phase, mark='x', killable = True):
        """
        Đánh dấu các nước có thể di chuyển của quân cờ
        :param nBoard: Bàn cờ (board.Board)
        :param index: Tạo độ quân cờ trên bàn cờ (tuple(int, int))
        :param mark: Kí hiệu dùng để đánh dấu (str)
        :param phase: Giai đoạn của lượt hiện tại (int)
        :param killable: Giá trị được gán cho thuộc tính killable của quân cờ (bool)
        :return Các vị trí mà quân cờ có thể đi (list(tuple(int, int)))
        """
        speed = self._speed
        oBoard = nBoard.getoBoard()
        rBoard = nBoard.getrBoard()

        direction = self.get_direction()

        self._MoveableCell = []

        controlledMark = 'x'
        if mark == '#':
            controlledMark = ' '
        else:
            for i in range(1, speed + 1):
                if '!' not in rBoard[index[0] + i * direction][index[1]] and oBoard[(index[1], index[0] + i * direction)] == None:
                    rBoard[index[0] + i * direction][index[1]] += controlledMark
                    self._MoveableCell.append((index[0] + i * direction, index[1]))
                elif '-' in rBoard[index[0] + i * direction][index[1]]:
                    rBoard[index[0] + i * direction][index[1]] += controlledMark
                    self._MoveableCell.append((index[0] + i * direction, index[1]))
                    break
                else:
                    break

        top3 = [[index[0] + direction * (speed > 0), index[1] + i * (speed > 0)] for i in range(-1, 2)]
        for positions in top3:
            try:
                if on_board(positions) and '!' not in rBoard[positions[0]][positions[1]] and rBoard[positions[0]][positions[1]] != '-':
                    if top3.index(positions) % 2 == 0:
                        try:
                            if oBoard[(positions[1], positions[0])].get_team() != self.get_team():
                                oBoard[(positions[1], positions[0])].set_killable(nBoard, positions, phase, killable)
                                if oBoard[(positions[1], positions[0])].get_killable():
                                    rBoard[positions[0]][positions[1]] += mark
                                    self._MoveableCell.append((positions[0], positions[1]))
                            elif mark == '#':
                                rBoard[positions[0]][positions[1]] += mark
                                self._MoveableCell.append((positions[0], positions[1]))

                        except:
                            if mark == '#':
                                rBoard[positions[0]][positions[1]] += mark
                            pass
                    else:
                        if rBoard[positions[0]][positions[1]] == ' ' and mark != '#':
                            rBoard[positions[0]][positions[1]] = controlledMark
                elif rBoard[positions[0]][positions[1]] == '-' and mark == '#':
                    rBoard[positions[0]][positions[1]] += mark
            except:
                pass

        return self._MoveableCell

class King(Chess):
    def __init__(self, team, direction, img, effects = []):
        """
        Khởi tạo quân "Vua"
        :param team: Tên đội (str)
        :param img: Hình ảnh quân cờ (pygame.image)
        :param effects: Danh sách hiệu ứng (list of str)
        """
        super().__init__(team, "King", direction, img, 10000, [ef.Effect('Unselectable', turns = -1, phase=[3]), ef.Effect('Unmove', turns = -1, phase=2)]  + effects, 1)

    def get_moves(self, nBoard, index, phase, mark='x', killable=True):
        """
        Đánh dấu các nước có thể di chuyển của quân cờ
        :param nBoard: Bàn cờ (board.Board)
        :param index: Tạo độ quân cờ trên bàn cờ (tuple(int, int))
        :param mark: Kí hiệu dùng để đánh dấu (str)
        :param phase: Giai đoạn của lượt hiện tại (int)
        :param killable: Giá trị được gán cho thuộc tính killable của quân cờ (bool)
        :return None
        """
        speed = self._speed
        oBoard = nBoard.getoBoard()
        rBoard = nBoard.getrBoard()

        self._MoveableCell = []

        for y in range(-speed, speed + 1):
            for x in range(-speed, speed + 1):
                if on_board((index[0] + y, index[1] + x)) and '!' not in rBoard[index[0] + y][index[1] + x]:
                    if '#' in rBoard[index[0] + y][index[1] + x] and mark == 'x':
                        pass
                    elif ' ' in rBoard[index[0] + y][index[1] + x]:
                        rBoard[index[0] + y][index[1] + x] = mark
                        self._MoveableCell.append((index[0] + y, index[1] + x))
                    else:
                        try:
                            if oBoard[(index[1] + x, index[0] + y)].get_team() != self.get_team():
                                oBoard[(index[1] + x, index[0] + y)].set_killable(nBoard, (index[0] + y, index[1] + x), phase, killable)
                                if oBoard[(index[1] + x, index[0] + y)].get_killable():
                                    rBoard[index[0] + y][index[1] + x] += mark
                                    self._MoveableCell.append((index[0] + y, index[1] + x))
                            elif mark == '#':
                                rBoard[index[0] + y][index[1] + x] += mark
                                self._MoveableCell.append((index[0] + y, index[1] + x))
                        except:
                            break

        if self.is_effective('Unmove') and '#' not in rBoard[index[0]][index[1]]:
            try:
                result0 = oBoard[index[0], 0].is_effective('Unmove')
            except:
                result0 = False
            if result0:
                for i in range(index[1] - 1, 0, -1):
                    if rBoard[index[0]][i] != ' ' and rBoard[index[0]][i] != 'x' or rBoard[index[0]][i] == '#':
                        print(rBoard[index[0]][i])
                        break
                    if mark != '#' and i == 1:
                        rBoard[index[0]][0] += 'x'
                        self._MoveableCell.append((0, 0))
            else:
                pass

            try:
                result1 = oBoard[index[0], 7].is_effective('Unmove')
            except:
                result1 = False
            if result1:
                for j in range(index[1] + 1, 7):
                    if (rBoard[index[0]][j] != ' ' and rBoard[index[0]][j] != 'x') or rBoard[index[0]][j] == '#':
                        print(rBoard[index[0]][j])
                        break
                    if mark != '#' and j == 6:
                        rBoard[index[0]][7] += 'x'
                        self._MoveableCell.append((0, 7))
            else:
                pass
        return self._MoveableCell

class Rook(Chess):
    def __init__(self, team, direction, img, effects = []):
        """
        Khởi tạo quân "Xa"
        :param team: Tên đội (str)
        :param img: Hình ảnh quân cờ (pygame.image)
        :param effects: Danh sách hiệu ứng (list of str)
        """
        super().__init__(team, "Rook", direction, img, 50, [ef.Effect('Unmove', turns = -1, phase=[2])] + effects, 8)

    def get_moves(self, nBoard, index, phase, mark='x', killable=True):
        """
        Đánh dấu các nước có thể di chuyển của quân cờ
        :param nBoard: Bàn cờ (board.Board)
        :param index: Tạo độ quân cờ trên bàn cờ (tuple(int, int))
        :param mark: Kí hiệu dùng để đánh dấu (str)
        :param phase: Giai đoạn của lượt hiện tại (int)
        :param killable: Giá trị được gán cho thuộc tính killable của quân cờ (bool)
        :return None
        """
        speed = self._speed
        oBoard = nBoard.getoBoard()
        rBoard = nBoard.getrBoard()

        self._MoveableCell = []

        cross = [[[index[0] + i, index[1]] for i in range(1, speed)],
                 [[index[0] - i, index[1]] for i in range(1, speed)],
                 [[index[0], index[1] + i] for i in range(1, speed)],
                 [[index[0], index[1] - i] for i in range(1, speed)]]

        for dir in cross:
            for pos in dir:
                if on_board(pos) and '!' not in rBoard[pos[0]][pos[1]]:
                    if ' ' not in rBoard[pos[0]][pos[1]] or '#' in rBoard[pos[0]][pos[1]]:
                        try:
                            if oBoard[(pos[1], pos[0])].get_team() != self.get_team():
                                oBoard[(pos[1], pos[0])].set_killable(nBoard, pos, phase, killable)
                                if oBoard[(pos[1], pos[0])].get_killable():
                                    rBoard[pos[0]][pos[1]] += mark
                                    self._MoveableCell.append((pos))
                            elif mark == '#':
                                rBoard[pos[0]][pos[1]] += mark
                            break
                        except:
                            rBoard[pos[0]][pos[1]] += mark
                            self._MoveableCell.append((pos))
                            if 'x' in rBoard[pos[0]][pos[1]] and mark == '#':
                                break
                    else:
                        rBoard[pos[0]][pos[1]] += mark
                        self._MoveableCell.append((pos))
                elif on_board(pos) and '!' in rBoard[pos[0]][pos[1]]:
                    break
        return self._MoveableCell

class Bishop(Chess):
    def __init__(self, team, direction, img, effects = []):
        """
        Khởi tạo quân "Tượng"
        :param team: Tên đội (str)
        :param img: Hình ảnh quân cờ (pygame.image)
        :param effects: Danh sách hiệu ứng (list of str)
        """
        super().__init__(team, "Bishop", direction, img, 30, effects, 8)

    def get_moves(self, nBoard, index, phase, mark='x', killable=True):
        """
        Đánh dấu các nước có thể di chuyển của quân cờ
        :param nBoard: Bàn cờ (board.Board)
        :param index: Tạo độ quân cờ trên bàn cờ (tuple(int, int))
        :param mark: Kí hiệu dùng để đánh dấu (str)
        :param phase: Giai đoạn của lượt hiện tại (int)
        :param killable: Giá trị được gán cho thuộc tính killable của quân cờ (bool)
        :return None
        """
        speed = self._speed
        oBoard = nBoard.getoBoard()
        rBoard = nBoard.getrBoard()

        self._MoveableCell = []

        diagonals = [[[index[0] + i, index[1] + i] for i in range(1, speed)],
                     [[index[0] + i, index[1] - i] for i in range(1, speed)],
                     [[index[0] - i, index[1] + i] for i in range(1, speed)],
                     [[index[0] - i, index[1] - i] for i in range(1, speed)]]

        for dir in diagonals:
            for pos in dir:
                if on_board(pos) and '!' not in rBoard[pos[0]][pos[1]]:
                    if ' ' not in rBoard[pos[0]][pos[1]] or '#' in rBoard[pos[0]][pos[1]]:
                        try:
                            if oBoard[(pos[1], pos[0])].get_team() != self.get_team():
                                oBoard[(pos[1], pos[0])].set_killable(nBoard, pos, phase, killable)
                                if oBoard[(pos[1], pos[0])].get_killable():
                                    rBoard[pos[0]][pos[1]] += mark
                                    self._MoveableCell.append((pos))
                            elif mark == '#':
                                rBoard[pos[0]][pos[1]] += mark
                            break
                        except:
                            rBoard[pos[0]][pos[1]] += mark
                            self._MoveableCell.append((pos))
                            if 'x' in rBoard[pos[0]][pos[1]] and mark == '#':
                                break
                    else:
                        rBoard[pos[0]][pos[1]] += mark
                        self._MoveableCell.append((pos))
                elif on_board(pos) and '!' in rBoard[pos[0]][pos[1]]:
                    break
        return self._MoveableCell

class Knight(Chess):
    def __init__(self, team, direction, img, effects = []):
        """
        Khởi tạo quân "Mã"
        :param team: Tên đội (str)
        :param img: Hình ảnh quân cờ (pygame.image)
        :param effects: Danh sách hiệu ứng (list of str)
        """
        super().__init__(team, "Knight", direction, img, 30, effects, 3)

    def get_moves(self, nBoard, index, phase, mark='x', killable=True):
        """
        Đánh dấu các nước có thể di chuyển của quân cờ
        :param nBoard: Bàn cờ (board.Board)
        :param index: Tạo độ quân cờ trên bàn cờ (tuple(int, int))
        :param mark: Kí hiệu dùng để đánh dấu (str)
        :param phase: Giai đoạn của lượt hiện tại (int)
        :param killable: Giá trị được gán cho thuộc tính killable của quân cờ (bool)
        :return None
        """
        speed = self._speed
        oBoard = nBoard.getoBoard()
        rBoard = nBoard.getrBoard()
        x = (speed - 1) * (-1)
        y = speed

        self._MoveableCell = []

        for i in range(x, y):
            for j in range(x, y):
                if abs(i) + abs(j) == y:
                    if on_board((index[0] + i, index[1] + j)) and '!' not in rBoard[index[0] + i][index[1] + j]:
                        if ' ' not in rBoard[index[0] + i][index[1] + j] or '#' in rBoard[index[0] + i][index[1] + j]:
                            try:
                                if oBoard[(index[1] + j, index[0] + i)].get_team() != self.get_team():
                                    oBoard[(index[1] + j, index[0] + i)].set_killable(nBoard, (index[0] + i, index[1] + j), phase, killable)
                                    if oBoard[(index[1] + j, index[0] + i)].get_killable():
                                        rBoard[index[0] + i][index[1] + j] += mark
                                        self._MoveableCell.append((index[0] + i, index[1] + j))
                            except:
                                rBoard[index[0] + i][index[1] + j] += mark
                                self._MoveableCell.append((index[0] + i, index[1] + j))
                        else:
                            rBoard[index[0] + i][index[1] + j] += mark
                            self._MoveableCell.append((index[0] + i, index[1] + j))

        return self._MoveableCell

class Queen(Chess):
    def __init__(self, team, direction, img, effects = []):
        """
        Khởi tạo quân "Hậu"
        :param team: Tên đội (str)
        :param img: Hình ảnh quân cờ (pygame.image)
        :param effects: Danh sách hiệu ứng (list of str)
        """
        super().__init__(team, "Queen", direction, img, 90, [ef.Effect('Unselectable', turns = -1, phase=[3])] + effects, 8)

    def get_moves(self, nBoard, index, phase, mark='x', killable=True):
        """
        Đánh dấu các nước có thể di chuyển của quân cờ
        :param nBoard: Bàn cờ (board.Board)
        :param index: Tạo độ quân cờ trên bàn cờ (tuple(int, int))
        :param mark: Kí hiệu dùng để đánh dấu (str)
        :param phase: Giai đoạn của lượt hiện tại (int)
        :param killable: Giá trị được gán cho thuộc tính killable của quân cờ (bool)
        :return None
        """
        oBoard = nBoard.getoBoard()
        rBoard = nBoard.getrBoard()
        speed = self._speed
        cross = [[[index[0] + i, index[1]] for i in range(1, speed)],
                 [[index[0] - i, index[1]] for i in range(1, speed)],
                 [[index[0], index[1] + i] for i in range(1, speed)],
                 [[index[0], index[1] - i] for i in range(1, speed)]]

        self._MoveableCell = []

        for dir in cross:
            for pos in dir:
                if on_board(pos) and '!' not in rBoard[pos[0]][pos[1]]:
                    if ' ' not in rBoard[pos[0]][pos[1]] or '#' in rBoard[pos[0]][pos[1]]:
                        try:
                            if oBoard[(pos[1], pos[0])].get_team() != self.get_team():
                                oBoard[(pos[1], pos[0])].set_killable(nBoard, pos, phase, killable)
                                if oBoard[(pos[1], pos[0])].get_killable():
                                    rBoard[pos[0]][pos[1]] += mark
                                    self._MoveableCell.append((pos))
                            elif mark == '#':
                                rBoard[pos[0]][pos[1]] += mark
                            break
                        except:
                            rBoard[pos[0]][pos[1]] += mark
                            self._MoveableCell.append((pos))
                            if 'x' in rBoard[pos[0]][pos[1]] and mark == '#':
                                break
                    else:
                        rBoard[pos[0]][pos[1]] += mark
                        self._MoveableCell.append((pos))
                elif on_board(pos) and '!' in rBoard[pos[0]][pos[1]]:
                    break

        diagonals = [[[index[0] + j, index[1] + j] for j in range(1, speed)],
                     [[index[0] + j, index[1] - j] for j in range(1, speed)],
                     [[index[0] - j, index[1] + j] for j in range(1, speed)],
                     [[index[0] - j, index[1] - j] for j in range(1, speed)]]

        for dir in diagonals:
            for pos in dir:
                if on_board(pos) and '!' not in rBoard[pos[0]][pos[1]]:
                    if ' ' not in rBoard[pos[0]][pos[1]] or '#' in rBoard[pos[0]][pos[1]]:
                        try:
                            if oBoard[(pos[1], pos[0])].get_team() != self.get_team():
                                oBoard[(pos[1], pos[0])].set_killable(nBoard, pos, phase, killable)
                                if oBoard[(pos[1], pos[0])].get_killable():
                                    rBoard[pos[0]][pos[1]] += mark
                                    self._MoveableCell.append((pos))
                            elif mark == '#':
                                rBoard[pos[0]][pos[1]] += mark
                            break
                        except:
                            rBoard[pos[0]][pos[1]] += mark
                            self._MoveableCell.append((pos))
                            if 'x' in rBoard[pos[0]][pos[1]] and mark == '#':
                                break
                    else:
                        rBoard[pos[0]][pos[1]] += mark
                        self._MoveableCell.append((pos))
                elif on_board(pos) and '!' in rBoard[pos[0]][pos[1]]:
                    break

        return self._MoveableCell