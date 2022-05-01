import pygame
import chess

class Card:
    def __init__(self, name, cost, img, descibe = '', skillCard = skillCard, selectedRequire = 0, effects = []):
        self.__name = name
        self.__startCost = cost
        self.__cost = self._startCost
        self.__img = img
        self.__effects = [ef.Effect('!')] + effects
        self.__describe = descibe
        self.__selected_require = selectedRequire
        self.__skillCard = skillCard

    def get_effects(self):
        """
        Lấy danh sách hiệu ứng của quân cờ.
        :return: Danh sách hiệu ứng của quân cờ (List of str)
        """
        return self.effects

    def draw(self, win, font, pos):
        """
        Vẽ hình ảnh lá bài trên cửa sổ
        :param win: Cửa sổ được chọn (pygame.display)
        :param pos: Vị trí hình ảnh được vẽ (tuple(x, y))
        """
        win.blit(self.__image, pos)
        win.blit(font.render(str(self.__cost), True, (0, 0, 0), (self.__img.get_width() * 0.8, self.__img.get_height() / 2)), pos)
        win.blit(font.render(self.__describe, True, (0, 0, 0), (self.__img.get_width() * 0.8, self.__img.get_height() / 2)), (pos[0] + self.__img.get_width() * 0.1, pos[1] + self.__img.get_height() / 2))

    def get_cost(self):
        """
        Lấy tiêu hao của lá bài
        :return: Tiêu hao của lá bài (int)
        """
        return self.__cost

    def set_cost(self, new_cost):
        """
        Gán tiêu hao mới của lá bài
        :param new_cost: Tiêu hao mới (int)
        """
        self.__cost = new_cost

    def get_selected_require(self):
        return self.__selected_require

    def play_card(self, oBoard, rBoard, index):
        def grant_effects(effects, oBoard, rBoard, lIndex):
            sChess.add_effect(effects)
        locals()[self.__typeCard](self.__effects, oBoard, rBoard, lIndex)