import pygame
import cell
import board
import effect as ef
import init
import chess
import random

class Environment:
    """
    Lớp 'Môi trường'
    """

    def __int__(self, name, image, width, effects = []):
        """
        Hàm tạo môi trường
        :param name: Tên môi trường (str)
        :param image: Danh sách hình ảnh môi trường (ditc(pygame.image))
        :param effect: Danh sách hiệu ứng của môi trường (list or str)
        """
        self._name = name
        self._image = image
        self._effects = effects
        self._width = width
        self._CellLayer = []

    def get_name(self):
        """
        Hàm lấy tên địa hình
        :return: Tên địa hình (str)
        """
        return self.__name

    def get_env_img(self):
        """
        Hàm lấy danh sách hình ảnh môi trường
        :return: Danh sách hình ảnh môi trường (ditc(pygame.image))
        """
        return self._image

    def get_effect(self):
        """
        Hàm lấy danh sách hiệu ứng
        :return: Hiệu ứng của môi trường(str)
        """
        return self.__effects

    def apply_env_effect(self, **options):
        pass

    def draw(self, win):
        interval = self._width / 8
        for row in range(8):
            for col in range(8):
                self._CellLayer[row][col].draw(win, interval, interval)

    def create_map(self, nBoard):
        cBoard = []
        interval = self._width / 8
        for x in range(8):
            cBoard.append([])
            for y in range(8):
                cBoard[x].append(cell.Cell((x * interval) + nBoard.get_y(), (y * interval) + nBoard.get_x(), self._image['Normal']))
        self._CellLayer = cBoard
        return cBoard

class Desert(Environment):
    """
    Lớp 'Sa mạc'
    """
    def __init__(self, image, width = 0, effects = []):
        """
        Hàm tạo môi trường sa mạc
        :param name: Tên môi trường (str)
        :param image: Danh sách hình ảnh môi trường (ditc(pygame.image))
        :param effect: Hiệu ứng của môi trường (str)
        """
        self.__efa_x = 0
        self.__efa_y = 0
        super().__int__('desert', image, width, 'Unmoveable')

    def create_map(self, nBoard):
        super().create_map(nBoard)

        for x in range(8):
            for y in range(8):
                self._CellLayer[x][y].set_img(self._image['Normal'])
        return self._CellLayer

    def apply_env_effect(self, nBoard, turn, phase):
        """
        Hàm áp dụng effect của môi trường 'Sa mạc' vào bàn cờ
        :param turn: Đếm ngược thời gian xuất hiện bão cát(int)
        """
        rBoard = nBoard.getrBoard()
        oBoard = nBoard.getoBoard()
        cBoard = nBoard.getcBoard()
        if phase == chess.PHASE['Start']:
            try:
                if turn%6 == 0:
                    self.__efa_x = random.randint(1, 4)
                    self.__efa_y = random.randint(0, 4)
                x = self.__efa_x
                y = self.__efa_y
                if turn%6 < 4:
                    for i in range(0, 3):
                        for j in range(4):
                            cBoard[j  + y][i + x].set_img(self._image['Special'])
                            try:
                                if oBoard[(j + y, i + x)] != None:
                                    oBoard[(j + y, i + x)].add_effect(ef.Effect('IncreaseSpeed', -10, turns = 1, phase = 2))
                            except:
                                pass
                elif turn%6 == 4:
                    self._CellLayer = self.create_map(nBoard)
                    nBoard.clear_map()
            except:
                pass

class Frozen_river(Environment):
    """
    Lớp 'Sông băng'
    """

    def __init__(self, image, width, effects = []):
        """
        Hàm tạo môi trường sông băng
        :param name: Tên môi trường (str)
        :param image: Danh sách hình ảnh môi trường (ditc(pygame.image))
        :param effect: Hiệu ứng của môi trường (str)
        """
        self._EffectedCells = {}
        super().__int__('frozen_river', image, width, 'Fall_Down')

    def create_map(self, nBoard):
        super().create_map(nBoard)
        cell_posision = list()
        count = int(0)
        self._EffectedCells = {}
        while (count < 12):
            x = random.randint(0, 7)
            y = random.randint(1, 6)
            if (x, y) in cell_posision:
                pass
            else:
                cell_posision.append((x, y))
                count += 1

        for (x, y) in cell_posision:
            self._CellLayer[x][y].set_img(self._image['Special'])
            self._EffectedCells.update({(x, y): 3})
        return self._CellLayer

    def apply_env_effect(self, nBoard, turn, phase):
        rBoard = nBoard.getrBoard()
        oBoard = nBoard.getoBoard()
        if phase == chess.PHASE['Start']:
            for x in range(8):
                for y in range(8):
                    try:
                        if rBoard[x][y] != ' ':
                            self._EffectedCells[(y, x)] -= 1
                        if self._EffectedCells[(y, x)] <= 0:
                            self._CellLayer[y][x].set_img(self._image['Triggered_effect'])
                            oBoard[(y, x)] = chess.Chess('', '!', '', '', effects=[ef.Effect('Unselectable', turns = 3)])
                            rBoard[x][y] = '!'
                            self._EffectedCells[(y, x)] -= 1
                            nBoard.printMap()
                        if self._EffectedCells[(y, x)] <= -4:
                            self._CellLayer[y][x].set_img(self._image['Special'])
                            self._EffectedCells[(y,x)] = 3
                            oBoard[(y, x)] = None
                            rBoard[x][y] = ' '
                    except:
                        pass



class Foggy_forest(Environment):
    """
    Lớp 'Rừng sương mù'
    """

    def __init__(self, image , width, effects = []):
        """
        Hàm tạo môi trường sông băng
        :param name: Tên môi trường (str)
        :param image: Danh sách hình ảnh môi trường (ditc(pygame.image))
        :param effect: Hiệu ứng của môi trường (str)
        """
        super().__int__('foggy_forest', image, width, 'Glamour')

    def create_map(self, nBoard):
        super().create_map(nBoard)

        for x in range(8):
            for y in range(8):
                self._CellLayer[x][y].set_img(self._image['Normal'])
        return self._CellLayer

    def apply_env_effect(self, nBoard, turn, phase):

        "Đổi toàn bộ ô cờ sang ô special"
        "Thay đổi giá trị di chuyển của quân cờ trừ mã xuống còn 4"
        rBoard = nBoard.getrBoard()
        oBoard = nBoard.getoBoard()
        cBoard = nBoard.getcBoard()
        if phase == chess.PHASE['Start']:
            try:
                if turn % 6 < 4:
                    for i in range(8):
                        for j in range(8):
                            cBoard[j][i].set_img(self._image['Special'])
                            try:
                                if oBoard[(j + y, i + x)] != None:
                                    oBoard[(j + y, i + x)].add_effect(ef.Effect('IncreaseSpeed', -4, turns=1, phase=2))
                            except:
                                pass
                elif turn % 6 == 4:
                    self._CellLayer = self.create_map(nBoard)
                    nBoard.clear_map()
            except:
                pass


class Swamp(Environment):
    """
    Lớp 'Đầm lầy'
    """

    def __init__(self, image , width, effects = []):
        """
        Hàm tạo môi trường đầm lầy
        :param name: Tên môi trường (str)
        :param image: Danh sách hình ảnh môi trường (ditc(pygame.image))
        :param effect: Hiệu ứng của môi trường (str)
        """
        super().__int__('swamp', image, width, effects)

    def apply_env_effect(self, nBoard, turn, phase):

        "Random vị trí 10 ô special"
        "Đổi ô cờ sang ô special"
        "Cài ô special như là 1 quân cờ"

class Grassland(Environment):
    """
    Lớp 'Thảo nguyên'
    """

    def __init__(self, image , width, effects = []):
        """
        Hàm tạo môi trường bình thường
        :param name: Tên môi trường (str)
        :param image: Danh sách hình ảnh môi trường (ditc(pygame.image))
        :param effect: Hiệu ứng của môi trường (str)
        """
        super().__int__('grassland', image, width, effects)

    def apply_env_effect(self, nBoard, turn, phase):
        pass

class Simp(Environment):
    def __init__(self, lImg, effects = []):
        super().__int__('Simp', lImg, effects)


#--------------------------
