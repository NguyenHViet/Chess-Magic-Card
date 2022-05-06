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
        super().__int__('desert', image, width, 'Unmoveable')

    def create_map(self, nBoard):
        super().create_map(nBoard)
        cell_posision = list()

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
        cell_posision = list()
        count = int(0)
        if phase == chess.PHASE['Start']:
            try:
                if turn%6 == 0:
                    while (count < 12):
                        x = random.randint(0, 7)
                        y = random.randint(1, 6)
                        if (x, y) in cell_posision:
                            pass
                        else:
                            cell_posision.append((x, y))
                            count += 1


                    for (x, y) in cell_posision:
                        self._CellLayer[x][y].set_img(self._image['Specical'])
                        try:
                            if nBoard.getoBoard()[(y, x)] != ' ':
                                nBoard.getoBoard()[(y, x)].add_effect(ef.Effect('IncreaseSpeed', value= -10, turn = 3, phase= 2, stack= 3))
                        except:
                            pass
                    nBoard.printMap()
                elif turn%6 == 3:
                    self._CellLayer = self.create_map(nBoard)
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
            self._CellLayer[x][y].set_img(self._image['Specical'])
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
                        if self._EffectedCells[(y, x)] <= -3:
                            self._CellLayer[y][x].set_img(self._image['Specical'])
                            self._EffectedCells[(y,x)] = 3
                            oBoard[(y, x)] = None
                            rBoard[x][y] = ' '
                    except:
                        pass



class Foggy_forest(Environment):
    """
    Lớp 'Rừng sương mù'
    """

    def __init__(self, image, effects = []):
        """
        Hàm tạo môi trường sông băng
        :param name: Tên môi trường (str)
        :param image: Danh sách hình ảnh môi trường (ditc(pygame.image))
        :param effect: Hiệu ứng của môi trường (str)
        """
        super().__int__('foggy_forest', image, 'Glamour')

    def apply_env_effect(self):

        "Đổi toàn bộ ô cờ sang ô speacial"
        "Thay đổi giá trị di chuyển của quân cờ trừ mã xuống còn 4"

class Swamp(Environment):
    """
    Lớp 'Đầm lầy'
    """

    def __init__(self, image, effects = []):
        """
        Hàm tạo môi trường đầm lầy
        :param name: Tên môi trường (str)
        :param image: Danh sách hình ảnh môi trường (ditc(pygame.image))
        :param effect: Hiệu ứng của môi trường (str)
        """
        super().__int__('swamp', image, effects)

    def apply_env_effect(self):

        "Random vị trí 10 ô speacial"
        "Đổi ô cờ sang ô speacial"
        "Cài ô speacial như là 1 quân cờ"

class Grassland(Environment):
    """
    Lớp 'Thảo nguyên'
    """

    def __init__(self, image, effects = []):
        """
        Hàm tạo môi trường bình thường
        :param name: Tên môi trường (str)
        :param image: Danh sách hình ảnh môi trường (ditc(pygame.image))
        :param effect: Hiệu ứng của môi trường (str)
        """
        super().__int__('grassland', image, effects)

class Simp(Environment):
    def __init__(self, lImg, effects = []):
        super().__int__('Simp', lImg, effects)


#--------------------------
