import pygame
import copy
import CMC.cell as cell
import CMC.effect as ef
import CMC.init as init
import CMC.chess as chess
import random

class Environment:
    """
    Lớp 'Môi trường'
    """
    def __int__(self, name, image, width, sfx = '', env_ef = ''):
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
        self._sfx = sfx
        self._env_ef = env_ef

    def duplication(self):
        """
        Tạo bản sao của môi trường
        :return: Bản sao môi trường (environment.Enviroment)
        """
        dup_env1 = copy.copy(self)
        dup_env1.set_img('')
        dup_env1.set_cellLayer([])
        dup_env1.set_env_sound('', [])
        dup_env2 = copy.deepcopy(dup_env1)
        return dup_env2

    def set_env_sound(self, new_sound = '', new_sfx = []):
        """
        Gán nhạc nền, âm thanh mới cho môi thường
        :param new_sound: Nhạc nền mới (pygame.mixer.Sound)
        :param new_sfx: Âm thanh mới (pygame.mixer.Sound)
        :return: None
        """
        """
        Gán nhạc nền, âm thanh mới cho môi thường
        :param new_sound: Nhạc nền mới (pygame.mixer.Sound)
        :param new_sfx: Âm thanh mới (pygame.mixer.Sound)
        :return: None
        """
        self._env_ef = new_sound
        self._sfx = new_sfx

    def set_img(self, new_img):
        """
        Gán hình ảnh mới
        :param new_img: Hình ảnh mới (pygame.image)
        :return: None
        """
        self._image = new_img

    def set_cellLayer(self, cellLayer):
        """
        Gán lớp ô cờ mới
        :param cellLayer: Lớp ô cờ mới (list(list(cell.Cell)))
        :return:
        """
        self._CellLayer = cellLayer

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

    def play_sfx(self, id):
        """
        Chạy các file âm thanh sfx
        :param id: ID trong list sfx (int)
        :return: None
        """
        try:
            self._sfx[0].set_volume(init.SETTINGS['Sound Volumn'] / 100)
            self._sfx[0].play()
        except:
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
        :param width: Kích thước bàn cờ (int)
        """
        self.__epos = (0, 0)
        self.__ewh = (0, 0)
        env_ef = pygame.mixer.Sound('assets/music/sand_storm.wav')
        super().__int__('desert', image, width, env_ef = env_ef)

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
                if turn%8 == 0:
                    self.__epos = (random.randint(1, 4), random.randint(0, 4))
                    self.__ewh = (random.randint(2, 3), random.randint(3, 4))
                x, y = self.__epos
                w, h = self.__ewh
                if turn%8 < 2:
                    for i in range(w):
                        for j in range(h):
                            self._CellLayer[j  + y][i + x].set_img(self._image['Prepare'])
                elif turn%8 == 2:
                    try:
                        self._env_ef.set_volume(init.SETTINGS['Sound Volumn'] / 100)
                        self._env_ef.play(-1)
                    except:
                        pass

                if turn%8 < 7 and turn%8 >= 2:
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
                elif turn%8 == 7:
                    self._CellLayer = self.create_map(nBoard)
                    for i in range(w):
                        for j in range(h):
                            try:
                                if '-' in oBoard[(j + y, i + x)].convert_to_readable():
                                    oBoard[(j + y, i + x)] = None
                            except:
                                pass
                    nBoard.clear_map()
                    try:
                        self._env_ef.stop()
                    except:
                        pass
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
        :param width: Kích thước bàn cờ (int)
        """
        self.__EffectedCells = {}
        sfx = [
            pygame.mixer.Sound('assets/music/ice_creak.wav'),
            pygame.mixer.Sound('assets/music/ice_creak_break.wav'),
            pygame.mixer.Sound('assets/music/ice_freeze.wav'),
        ]
        super().__int__('frozen_river', image, width, sfx = sfx)

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
                                self.play_sfx(0)
                                self._CellLayer[y][x].set_img(self._image['Special 2'])
                        elif self.__EffectedCells[(y, x)] < 4:
                            self.__EffectedCells[(y, x)] = 4
                            self._CellLayer[y][x].set_img(self._image['Special'])
                        if self.__EffectedCells[(y, x)] <= 0:
                            self.play_sfx(1)
                            self._CellLayer[y][x].set_img(self._image['Triggered_effect'])
                            oBoard[(y, x)] = chess.Chess('', '!', '', '', effects=[ef.Effect('Unselectable', turns = 3)])
                            rBoard[x][y] = '!'
                            self.__EffectedCells[(y, x)] -= 1
                        if self.__EffectedCells[(y, x)] <= -4:
                            self.play_sfx(2)
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
        :param width: Kích thước bàn cờ (int)
        """
        env_ef = pygame.mixer.Sound('assets/music/foggy_forest.wav')
        super().__int__('foggy_forest', image, width, env_ef = env_ef)

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
                    try:
                        self._env_ef.set_volume(init.SETTINGS['Sound Volumn'] / 100)
                        self._env_ef.play(-1, fade_ms=1000)
                    except:
                        pass
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
                    try:
                        self._env_ef.stop()
                    except:
                        pass
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
        :param width: Kích thước bàn cờ (int)
        """
        self.__EffectedCells = {}
        sfx = [pygame.mixer.Sound('assets/music/step_into_mud.wav')]
        super().__int__('swamp', image, width, sfx = sfx)

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

class Echoes_Of_The_Past(Environment):
    """
    Lớp 'Dư âm của quá khứ'
    """
    def __init__(self, image, width):
        """
        Hàm tạo môi trường 'Dư âm của quá khứ'
        :param image: Danh sách hình ảnh môi trường (ditc(pygame.image))
        :param width: Kích thước bàn cờ (int)
        """
        self.__The_past = None
        env = pygame.mixer.Sound('assets/music/Church Bells.wav')
        super().__int__('echoes_of_the_past', image, width, env_ef = env)

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
        cBoard = nBoard.getcBoard()
        oBoard = nBoard.getoBoard()
        rBoard = nBoard.getrBoard()

        if phase == chess.PHASE['Start']:
            try:
                if turn%10 == 6:
                    if self.__The_past != None:
                        self.__The_past = None
                    self.__The_past = nBoard.duplication()

                if (turn%10 == 8) or (turn%10 == 9):
                    try:
                        self._env_ef.set_volume(init.SETTINGS['Sound Volumn'] / 100)
                        self._env_ef.play(2)
                    except:
                        pass
                    self._env_ef.set_volume(init.SETTINGS['Sound Volumn'] / 100)
                    self._env_ef.play()
                    for i in range(8):
                        for j in range(8):
                            cBoard[j][i].set_img(self._image['Special'])

                if (turn%10 == 0) and (turn != 0):
                    self._CellLayer = self.create_map(nBoard)
                    nBoard.clear_map()

                    for i in range(8):
                        for j in range(8):
                            try:
                                oBoard[(i, j)] = self.__The_past.getoBoard()[(i, j)]
                                if oBoard[(i, j)].get_team() == 'w':
                                    if oBoard[(i, j)].get_type() == 'Pawn':
                                        oBoard[(i, j)].set_img(init.listImage['w']['Pawn'])
                                    if oBoard[(i, j)].get_type() == 'Rook':
                                        oBoard[(i, j)].set_img(init.listImage['w']['Rook'])
                                    if oBoard[(i, j)].get_type() == 'Knight':
                                        oBoard[(i, j)].set_img(init.listImage['w']['Knight'])
                                    if oBoard[(i, j)].get_type() == 'Bishop':
                                        oBoard[(i, j)].set_img(init.listImage['w']['Bishop'])
                                    if oBoard[(i, j)].get_type() == 'Queen':
                                        oBoard[(i, j)].set_img(init.listImage['w']['Queen'])
                                    if oBoard[(i, j)].get_type() == 'King':
                                        oBoard[(i, j)].set_img(init.listImage['w']['King'])
                                if oBoard[(i, j)].get_team() == 'b':
                                    if oBoard[(i, j)].get_type() == 'Pawn':
                                        oBoard[(i, j)].set_img(init.listImage['b']['Pawn'])
                                    if oBoard[(i, j)].get_type() == 'Rook':
                                        oBoard[(i, j)].set_img(init.listImage['b']['Rook'])
                                    if oBoard[(i, j)].get_type() == 'Knight':
                                        oBoard[(i, j)].set_img(init.listImage['b']['Knight'])
                                    if oBoard[(i, j)].get_type() == 'Bishop':
                                        oBoard[(i, j)].set_img(init.listImage['b']['Bishop'])
                                    if oBoard[(i, j)].get_type() == 'Queen':
                                        oBoard[(i, j)].set_img(init.listImage['b']['Queen'])
                                    if oBoard[(i, j)].get_type() == 'King':
                                        oBoard[(i, j)].set_img(init.listImage['b']['King'])
                                rBoard[(i, j)] = The_past.getrBoard()[(i, j)]
                            except:
                                pass
                    try:
                        self._env_ef.stop()
                    except:
                        pass
            except:
                pass

class Grassland(Environment):
    """
    Lớp 'Thảo nguyên'
    """

    def __init__(self, image , width):
        """
        Hàm tạo môi trường 'Thảo Nguyên'
        :param name: Tên môi trường (str)
        :param image: Danh sách hình ảnh môi trường (ditc(pygame.image))
        :param width: Kích thước bàn cờ (int)
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
