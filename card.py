import copy

import pygame
import chess
import effect as ef
import cell
import init
import textwrap

def drawText(surface, text, color, rect, font, aa=False, bkg=None):
    rect = pygame.Rect(rect)
    y = rect.top
    lineSpacing = -2
    fontHeight = font.size("Tg")[1]
    while text:
        i = 1
        if y + fontHeight > rect.bottom:
            break
        while font.size(text[:i])[0] < rect.width and i < len(text):
            i += 1

        if i < len(text):
            i = text.rfind(" ", 0, i) + 1
        if bkg:
            image = font.render(text[:i], 1, color, bkg)
            image.set_colorkey(bkg)
        else:
            image = font.render(text[:i], aa, color)
        surface.blit(image, (rect.left, y))
        y += fontHeight + lineSpacing
        text = text[i:]
    return text


class Card:
    def __init__(self, name, cost, img, descibe = '', skillCard = '', selectedRequire = 0, effects = [], **options):
        self.__name = name
        self.__startCost = cost
        self.__cost = self.__startCost
        self.__img = img
        self.__effects = [] + effects
        self.__describe = descibe
        self.__selected_require = selectedRequire
        self.__skillCard = skillCard
        self.__options = options

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
        cheight = self.__img.get_height()
        cwidth = self.__img.get_width()
        nwidth = (height/cheight)*cwidth
        offsetHeight = (height - cheight)/2
        offsetWidth = (width - cwidth)/2
        win.blit(self.__img, (pos[0] + offsetWidth, pos[1] + offsetHeight))
        textSurface = font.render(str(self.__cost), True, 'white')
        textRect = textSurface.get_rect()
        textRect.center = ((pos[0] + 57.5), (pos[1]) + 40)
        win.blit(textSurface, textRect)

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

    def play_card(self, nBoard, indexs, playTeam):
        def GrantEffects(effects, nBoard, indexs):
            try:
                index = indexs[0]
                oBoard = nBoard.getoBoard()
                nBoard.select_Chess(index, 3, playTeam, False)
                for effect in effects:
                    oBoard[(index[1], index[0])].add_effect(copy.copy(effect))
                return 'Casted'
            except:
                return ef.STATUS[1]

        def ActiveEffects(effects, nBoard, indexs):
            phase = 3
            result = []
            for effect in effects:
                try:
                    result.append(copy.copy(effect).active_effect(nBoard, indexs, 3, options = self.__options, playTeam = playTeam))
                    effect.unactive_effect()
                except:
                    result.append(ef.STATUS[1])
            if ef.STATUS[3] in result:
                result[result.index(ef.STATUS[3])] = 'Casted'
            return result
        try:
            result = locals()[self.__skillCard](self.__effects, nBoard, indexs)
        except:
            result = 'Fail'
        return result

class CardArea:
    def __init__(self, height, width, offsetHeight, offsetWidth, lImg):
        self.__x = offsetHeight
        self.__y = offsetWidth + width
        self.__Height = height
        self.__Width = offsetWidth - 40
        self.__cellLayers = []
        self.__GEI = lImg['GEI']
        self.__picking = None
        interval = (height + 10) / 3
        for i in range(3):
            self.__cellLayers.append(cell.Cell(self.__y + 55, self.__x + interval * i, self.__GEI['Darken']))

    def draw(self, win, font, pos, nPlayer):
        listCard = nPlayer.get_cards()
        picking = nPlayer.get_picking()
        interval = self.__Height / 3
        for cell in self.__cellLayers:
            if cell.is_mouse_hovering(pos):
                cell.set_img(self.__GEI['Card_Hover'])
            else:
                cell.set_img(self.__GEI['Empty'])
            try:
                self.__cellLayers[picking].set_img(self.__GEI['Card_Picking'])
            except:
                pass
            cell.draw(win, interval, self.__Width - 20)
        for i in range(len(listCard)):
            listCard[i].draw(win, font, self.__cellLayers[i].get_pos(), self.__Height / 3, self.__Width)
            if listCard[i].get_cost() > nPlayer.get_action():
                win.blit(init.listImage['GEI']['LockCard'], self.__cellLayers[i].get_pos())

    def pick_card(self, pos):
        for i in range(3):
            if self.__cellLayers[i].is_mouse_hovering(pos):
                return i
        return None