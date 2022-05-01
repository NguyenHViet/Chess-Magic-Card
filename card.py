import pygame
import chess

class Card:
    def __init__(self, name, cost, img, descibe, effects = []):
        self._name = name
        self._startCost = cost
        self._cost = self._startCost
        self._img = img
        self._effects = [ef.Effect('!')] + effects
        self._describe = descibe

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
        win.blit(self.image, pos)
        win.blit(font.render(str(self._cost), True, (0, 0, 0), (self._img.get_width() * 0.8, self._img.get_height() / 2)), pos)
        win.blit(font.render(self._describe, True, (0, 0, 0), (self._img.get_width() * 0.8, self._img.get_height() / 2)), (pos[0] + self._img.get_width() * 0.1, pos[1] + self._img.get_height() / 2))

    def get_cost(self):
        """
        Lấy tiêu hao của lá bài
        :return: Tiêu hao của lá bài (int)
        """
        return self._cost

    def set_cost(self, new_cost):
        """
        Gán tiêu hao mới của lá bài
        :param new_cost: Tiêu hao mới (int)
        """
        self._cost = new_cost

    def