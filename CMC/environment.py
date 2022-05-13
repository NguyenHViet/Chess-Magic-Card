import pygame
import CMC.cell as cell
import CMC.effect as ef
import CMC.init as init
import CMC.chess as chess
import random

class Environment:
    """
    Lớp 'Môi trường'
    """
    def __int__(self, name, image, width):
        """
        Hàm khởi tạo
        :param name: Tên môi trường (str)
        :param image: Danh sách hình ảnh của môi trường (dict)
        :param width: Kích thước bàn cờ (int)
        """
        self._name = name
        self._image = image
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
        :return: Danh sách hình ảnh môi trường (dict(pygame.image))
        """
        return self._image

    def apply_env_effect(self, **options):
        """
        Hàm áp dụng hiệu ứng môi trường
        :param options: các giá trị tùy chọn
        """
        pass

    def draw(self, win):
        """
        Hàm in các hình ảnh lên cửa sổ hiển thị
        :param win: Cửa sổ hiển thị (pygame.display)
        :return None
        """
        win.blit(self._image['Background'], (0, 0))
        #win.blit(pygame.transform.scale(init.listImage['GEI']['Darken'], (1600, 1000)), (0, 0))
        interval = self._width / 8
        for row in range(8):
            for col in range(8):
                self._CellLayer[row][col].draw(win, interval, interval)

    def create_map(self, nBoard):
        """
        Khởi tạo bàn cờ theo môi trường
        :param nBoard: Bàn cờ (board.Board)
        :return: Danh sách 2D các ô trong bàn cờ (list(list))
        """
        cBoard = []
        interval = self._width / 8
        for x in range(8):
            cBoard.append([])
            for y in range(8):
                cBoard[x].append(
                    cell.Cell((x * interval) + nBoard.get_y(), (y * interval) + nBoard.get_x(), self._image['Normal']))
        self._CellLayer = cBoard
        return cBoard

    def play_sfx(self):
        pass

class Desert(Environment):
    """
    Lớp 'Sa mạc'
    """
    def __init__(self, image, width = 0):
        """
        Hàm tạo môi trường "Sa Mạc"
        :param name: Tên môi trường (str)
        :param image: Danh sách hình ảnh môi trường (ditc(pygame.image))
        """
        self.__epos = (0, 0)
        self.__ewh = (0, 0)
        self.__env_ef = pygame.mixer.Sound('assets/music/sand_storm.wav')
        super().__int__('desert', image, width)

    def create_map(self, nBoard):
        """
        Khởi tạo bàn cờ theo môi trường
        :param nBoard: Bàn cờ (board.Board)
        :return: Danh sách 2D các ô trong bàn cờ (list(list))
        """
        super().create_map(nBoard)
        return self._CellLayer

    def apply_env_effect(self, nBoard, turn, phase):
        """
        Hàm áp dụng hiệu ứng môi trường
        :param nBoard: Bàn cờ (board.Board)
        :param turn: Lượt hiện tại của trận đấu
        :param phase: Giai đoạn của lượt hiện tại (int)
        :return None
        """
        rBoard = nBoard.getrBoard()
        oBoard = nBoard.getoBoard()
        cBoard = nBoard.getcBoard()
        if phase == chess.PHASE['Start']:
            try:
                if turn%6 == 0:
                    self.__epos = (random.randint(1, 4), random.randint(0, 4))
                    self.__ewh = (random.randint(2, 3), random.randint(3, 4))
                x, y = self.__epos
                w, h = self.__ewh
                if turn%6 < 2:
                    for i in range(w):
                        for j in range(h):
                            self._CellLayer[j  + y][i + x].set_img(self._image['Prepare'])
                elif turn%6 == 2:
                    self.__env_ef.set_volume(init.SETTINGS['Sound Volumn'] / 100)
                    self.__env_ef.play(-1)

                if turn%6 < 5 and turn%6 >= 2:
                    for i in range(w):
                        for j in range(h):
                            cBoard[j  + y][i + x].set_img(self._image['Special'])
                            try:
                                if oBoard[(j + y, i + x)] != None:
                                    oBoard[(j + y, i + x)].add_effect(ef.Effect('IncreaseSpeed', -10, turns = 1, phase = 2))
                                else:
                                    oBoard[(j + y, i + x)] = chess.Chess('-', '', '', '')
                            except:
                                pass
                elif turn%6 == 5:
                    self._CellLayer = self.create_map(nBoard)
                    for i in range(w):
                        for j in range(h):
                            try:
                                if '-' in oBoard[(j + y, i + x)].convert_to_readable():
                                    oBoard[(j + y, i + x)] = None
                            except:
                                pass
                    nBoard.clear_map()
                    self.__env_ef.stop()
            except:
                pass

class Frozen_river(Environment):
    """
    Lớp 'Sông băng'
    """

    def __init__(self, image, width):
        """
        Hàm khởi tạo môi trường "Sông Băng"
        :param name: Tên môi trường (str)
        :param image: Danh sách hình ảnh môi trường (ditc(pygame.image))
        """
        self.__EffectedCells = {}
        self.__sfx = [
            pygame.mixer.Sound('assets/music/ice_creak.wav'),
            pygame.mixer.Sound('assets/music/ice_creak_break.wav'),
            pygame.mixer.Sound('assets/music/ice_freeze.wav'),
        ]
        super().__int__('frozen_river', image, width)

    def create_map(self, nBoard):
        """
        Khởi tạo bàn cờ theo môi trường
        :param nBoard: Bàn cờ (board.Board)
        :return: Danh sách 2D các ô trong bàn cờ (list(list))
        """
        super().create_map(nBoard)
        cell_posision = list()
        count = int(0)
        self.__EffectedCells = {}
        while (count < 12):
            x = random.randint(0, 7)
            y = random.randint(2, 5)
            if (x, y) in cell_posision:
                pass
            else:
                cell_posision.append((x, y))
                count += 1

        for (x, y) in cell_posision:
            self._CellLayer[x][y].set_img(self._image['Special'])
            self.__EffectedCells.update({(x, y): 3})
        return self._CellLayer

    def apply_env_effect(self, nBoard, turn, phase):
        """
        Hàm áp dụng hiệu ứng môi trường
        :param nBoard: Bàn cờ (board.Board)
        :param turn: Lượt hiện tại của trận đấu
        :param phase: Giai đoạn của lượt hiện tại (int)
        :return None
        """
        rBoard = nBoard.getrBoard()
        oBoard = nBoard.getoBoard()
        if phase == chess.PHASE['Start']:
            for x in range(8):
                for y in range(8):
                    try:
                        if oBoard[(y, x)] != None:
                            self.__EffectedCells[(y, x)] -= 1
                            if self.__EffectedCells[(y, x)] <= 2:
                                self.__sfx[0].set_volume(init.SETTINGS['Sound Volumn'] / 100)
                                self.__sfx[0].play()
                                self._CellLayer[y][x].set_img(self._image['Special 2'])
                        elif self.__EffectedCells[(y, x)] < 4:
                            self.__EffectedCells[(y, x)] = 4
                            self._CellLayer[y][x].set_img(self._image['Special'])
                        if self.__EffectedCells[(y, x)] <= 0:
                            self.__sfx[1].set_volume(init.SETTINGS['Sound Volumn'] / 100)
                            self.__sfx[1].play()
                            self._CellLayer[y][x].set_img(self._image['Triggered_effect'])
                            oBoard[(y, x)] = chess.Chess('', '!', '', '', effects=[ef.Effect('Unselectable', turns = 3)])
                            rBoard[x][y] = '!'
                            self.__EffectedCells[(y, x)] -= 1
                        if self.__EffectedCells[(y, x)] <= -4:
                            self.__sfx[2].set_volume(init.SETTINGS['Sound Volumn'] / 100)
                            self.__sfx[2].play()
                            self._CellLayer[y][x].set_img(self._image['Special'])
                            self.__EffectedCells[(y,x)] = 4
                            oBoard[(y, x)] = None
                            rBoard[x][y] = ' '
                    except:
                        pass



class Foggy_forest(Environment):
    """
    Lớp 'Rừng sương mù'
    """
    def __init__(self, image , width):
        """
        Hàm tạo môi trường "Rừng Sương Mù"
        :param name: Tên môi trường (str)
        :param image: Danh sách hình ảnh môi trường (ditc(pygame.image))
        """
        self.__env_ef = pygame.mixer.Sound('assets/music/foggy_forest.wav')
        super().__int__('foggy_forest', image, width)

    def create_map(self, nBoard):

        super().create_map(nBoard)

        for x in range(8):
            for y in range(8):
                self._CellLayer[x][y].set_img(self._image['Normal'])
        return self._CellLayer

    def apply_env_effect(self, nBoard, turn, phase):
        """
        Hàm áp dụng hiệu ứng môi trường
        :param nBoard: Bàn cờ (board.Board)
        :param turn: Lượt hiện tại của trận đấu
        :param phase: Giai đoạn của lượt hiện tại (int)
        :return None
        """
        rBoard = nBoard.getrBoard()
        oBoard = nBoard.getoBoard()
        cBoard = nBoard.getcBoard()
        if phase == chess.PHASE['Start']:
            try:
                if turn % 6 == 0:
                    self.__env_ef.set_volume(init.SETTINGS['Sound Volumn'] / 100)
                    self.__env_ef.play(fade_ms=1000)
                if turn % 6 < 4:
                    for i in range(8):
                        for j in range(8):
                            cBoard[j][i].set_img(self._image['Special'])
                            try:
                                if oBoard[(j, i)] != None:
                                    if oBoard[(j, i)].get_type() not in ['Knight', 'Pawn']:
                                        oBoard[(j, i)].add_effect(ef.Effect('IncreaseSpeed', -4, turns=1, phase=2))
                            except:
                                pass
                elif turn % 6 == 4:
                    self._CellLayer = self.create_map(nBoard)
                    nBoard.clear_map()
                    self.__env_ef.stop()
            except:
                pass


class Swamp(Environment):
    """
    Lớp 'Đầm lầy'
    """

    def __init__(self, image , width):
        """
        Hàm tạo môi trường "Đầm Lầy"
        :param name: Tên môi trường (str)
        :param image: Danh sách hình ảnh môi trường (ditc(pygame.image))
        """
        self.__EffectedCells = {}
        self.__sfx = pygame.mixer.Sound('assets/music/step_into_mud.wav')
        super().__int__('swamp', image, width)

    def create_map(self, nBoard):
        super().create_map(nBoard)
        cell_posision = list()
        count = int(0)
        self.__EffectedCells = {}
        while (count < 10):
            x = random.randint(0, 7)
            y = random.randint(1, 6)
            if (x, y) in cell_posision:
                pass
            else:
                cell_posision.append((x, y))
                count += 1

        for (x, y) in cell_posision:
            self._CellLayer[x][y].set_img(self._image['Special'])
            self.__EffectedCells.update({(x, y): None})
        return self._CellLayer

    def apply_env_effect(self, nBoard, turn, phase):
        """
        Hàm áp dụng hiệu ứng môi trường
        :param nBoard: Bàn cờ (board.Board)
        :param turn: Lượt hiện tại của trận đấu
        :param phase: Giai đoạn của lượt hiện tại (int)
        :return None
        """
        rBoard = nBoard.getrBoard()
        oBoard = nBoard.getoBoard()
        if phase == chess.PHASE['Start']:
            for x in range(8):
                for y in range(8):
                    try:
                        if rBoard[x][y] == ' ' and (y, x) in self.__EffectedCells.keys():
                            oBoard[(y, x)] = chess.Chess('-', '', '', '')
                    except:
                        pass

    def play_sfx(self):
        self.__sfx.set_volume(init.SETTINGS['Sound Volumn'] / 100)
        self.__sfx.play()

class Grassland(Environment):
    """
    Lớp 'Thảo nguyên'
    """

    def __init__(self, image , width):
        """
        Hàm tạo môi trường 'Thảo Nguyên'
        :param name: Tên môi trường (str)
        :param image: Danh sách hình ảnh môi trường (ditc(pygame.image))
        """
        super().__int__('grassland', image, width)

    def apply_env_effect(self, nBoard, turn, phase):
        """
        Hàm áp dụng hiệu ứng môi trường
        :param nBoard: Bàn cờ (board.Board)
        :param turn: Lượt hiện tại của trận đấu
        :param phase: Giai đoạn của lượt hiện tại (int)
        :return None
        """
        pass


#--------------------------
