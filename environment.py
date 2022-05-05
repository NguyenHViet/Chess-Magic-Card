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

    def __int__(self, name, image, effects = []):
        """
        Hàm tạo môi trường
        :param name: Tên môi trường (str)
        :param image: Danh sách hình ảnh môi trường (ditc(pygame.image))
        :param effect: Danh sách hiệu ứng của môi trường (list or str)
        """
        self.__name = name
        self.__image = image
        self.__effects = effects

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
        return self.__image

    def get_effect(self):
        """
        Hàm lấy danh sách hiệu ứng
        :return: Hiệu ứng của môi trường(str)
        """
        return self.__effects

    def apply_env_effect(self, **options):
        pass

class Desert(Environment):
    """
    Lớp 'Sa mạc'
    """
    def __init__(self, image, effects = []):
        """
        Hàm tạo môi trường sa mạc
        :param name: Tên môi trường (str)
        :param image: Danh sách hình ảnh môi trường (ditc(pygame.image))
        :param effect: Hiệu ứng của môi trường (str)
        """
        super().__int__('desert', image, 'Unmoveable')

    def apply_env_effect(self, nBoard, turn, phase):
        """
        Hàm áp dụng effect của môi trường 'Sa mạc' vào bàn cờ
        :param turn: Đếm ngược thời gian xuất hiện bão cát(int)
        """
        if phase == chess.PHASE['start']:
            try:
                if turn%6 == 0:
                    area = random.Random.randint(1, 5)
                    if area == 1:
                        count_1 = int(0)
                        count_2 = int(0)
                    elif area ==2:
                        count_1 = int(0)
                        count_2 = int(4)
                    elif area == 3:
                        count_1 = int(3)
                        count_2 = int(0)
                    elif area == 4:
                        count_1 = int(3)
                        count_2 = int(4)
                    area_effect = list[list]

                    for i in range(1, 4):
                        for j in range(4):
                            board.Board.getcBoard()[j + count_2][i + count_1].set_img(init.listImage['Environment']['Speacial'])
                            try:
                                if board.Board.getoBoard()[(j + count_2, i + count_1)] != None:
                                    board.Board.getoBoard()[(j + count_2, i + count_1)].add_effect(ef.Effect(self.get_effect(), 0, 1, 2, 0, True))
                            except:
                                pass
            except:
                pass

class Frozen_river(Environment):
    """
    Lớp 'Sông băng'
    """

    def __init__(self, image, effects = []):
        """
        Hàm tạo môi trường sông băng
        :param name: Tên môi trường (str)
        :param image: Danh sách hình ảnh môi trường (ditc(pygame.image))
        :param effect: Hiệu ứng của môi trường (str)
        """
        super().__int__('frozen_river', image, 'Fall_Down')

    def apply_env_effect(self, nBoard, turn, phase):
        env_obj = chess.Chess('env_obj')



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
