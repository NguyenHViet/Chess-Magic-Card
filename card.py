import pygame
import chess
import effect as ef
import cell

class Card:
    def __init__(self, name, cost, img, descibe = '', skillCard = '', selectedRequire = 0, effects = []):
        self.__name = name
        self.__startCost = cost
        self.__cost = self.__startCost
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

    def draw(self, win, font, pos, height = 100, width = 100):
        """
        Vẽ hình ảnh lá bài trên cửa sổ
        :param win: Cửa sổ được chọn (pygame.display)
        :param pos: Vị trí hình ảnh được vẽ (tuple(x, y))
        """
        self.__img = pygame.transform.scale(self.__img, (width, height))
        win.blit(self.__img, pos)
        win.blit(font.render(str(self.__cost), True, (0, 0, 0)), pos)
        info = pygame.transform.scale(font.render(self.__describe, True, (0, 0, 0)), (width * 0.8, height / 2))
        win.blit(info, (pos[0] + self.__img.get_width() * 0.1, pos[1] + self.__img.get_height() / 2))

#, (self.__img.get_width() * 0.8, self.__img.get_height() / 2)
#

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

    def play_card(self, oBoard, rBoard, indexs):
        def GrantEffects(effects, oBoard, rBoard, indexs):
            sChess.add_effect(effects)
        locals()[self.__typeCard](self.__effects, oBoard, rBoard, indexs)

class CardArea:
    def __init__(self, height, width, offsetHeight, offsetWidth, lImg):
        self.__x = offsetHeight
        self.__y = offsetWidth + width
        self.__Height = height
        self.__Width = offsetWidth
        self.__cellLayers = []
        self.__GEI = lImg['GEI']
        interval = (height + 10) / 3
        for i in range(3):
            self.__cellLayers.append(cell.Cell(self.__y + 10, self.__x + interval * i, self.__GEI['Darken']))

    def draw(self, win, font, pos, listCard = [], picking = -1):
        interval = self.__Height / 3
        for cell in self.__cellLayers:
            if cell.is_mouse_hovering(pos):
                cell.set_img(self.__GEI['Choice'])
            else:
                cell.set_img(self.__GEI['Darken'])
            cell.draw(win, interval, self.__Width - 20)
        for i in range(len(listCard)):
            listCard[i].draw(win, font, self.__cellLayers[i].get_pos(), self.__Height / 3, self.__Width)

    def pick_card(self, pos):
        for i in range(3):
            if self.__cellLayers[i].is_mouse_hovering(pos):
                return i
        return None