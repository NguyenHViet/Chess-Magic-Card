import copy

import pygame
import CMC.effect as ef
import CMC.cell as cell
import CMC.init as init


def drawText(surface, text, color, rect, font, bkg=None):
    """
    Hàm dùng để tạo text có thể format xuống dòng
    :param surface: Surface được chọn để hiển thị (pygame.display)
    :param text: Văn bản được in (str)
    :param color: Màu sắc văn bản (str|(int, int, int)
    :param rect: Tạo độ góc trên bên trái và kích thước (((float, float), (float, float)))
    :param font: Font chữ của văn bản (font.Font)
    :param bkg: Màu nền (str|(int, int, int)
    :return: Văn bản đã được format (str)
    """
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
            image = font.render(text[:i], False, color)
        surface.blit(image, (rect.left, y))
        y += fontHeight + lineSpacing
        text = text[i:]
    return text


class Card:
    """
    Lớp "Bài phép"
    """
    def __init__(self, name, cost, img, descibe = '', skillCard = '', selectedRequire = 0, effects = [], **options):
        """
        Hàm khởi tạo bài phép
        :param name: Tên bài phép (str)
        :param cost: Giá trị tiêu hao (int)
        :param img: Hình ảnh bài phép (pygame.image)
        :param descibe: Mô tả (str)
        :param skillCard: Tên kĩ năng của bài phép (str)
        :param selectedRequire: Số lượng quân cờ cần thiết (int)
        :param effects: Hiệu ứng bài phép (effect.Effect)
        :param options: Các giá trị tùy chọn
        """
        self.__name = name
        self.__startCost = cost
        self.__cost = self.__startCost
        self.__img = img
        self.__effects = [] + effects
        self.__describe = descibe
        self.__selected_require = selectedRequire
        self.__skillCard = skillCard
        self.__options = options

    def duplication(self):
        """
        Tạo bản sao của lá bài
        :return: Bản sao của lá bài (card.Card)
        """
        dup_card1 = copy.copy(self)
        dup_card1.set_img('')
        dup_card2 = copy.deepcopy(dup_card1)
        return dup_card2

    def set_img(self, new_img):
        """
        Gán hình ảnh mới
        :param new_img: Hình ảnh mới (pygame.image)
        :return: None
        """
        self.__img = new_img

    def get_effects(self):
        """
        Lấy danh sách hiệu ứng của quân cờ.
        :return: Danh sách hiệu ứng của quân cờ (list(effect.Effect))
        """
        return self.effects

    def get_name(self):
        """
        Lấy tên lá bài
        :return: Tên lá bài (str)
        """
        return self.__name

    def draw(self, win, font, pos, height = 100, width = 100):
        """
        Vẽ hình ảnh lá bài trên cửa sổ hiển thị
        :param win: Cửa sổ hiển thị được chọn (pygame.display)
        :param pos: Vị trí hình ảnh được vẽ (tuple(int, int))
        :return None
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
        :return None
        """
        self.__cost = new_cost

    def get_selected_require(self):
        """
        Lấy số lượng quân cờ cần thiết để sử dụng phép
        :return: Số lượng quân cờ cần thiết (int)
        """
        return self.__selected_require

    def play_card(self, nBoard, indexs, playTeam, histLog=False):
        """
        Sử dụng bài phép và kích hoạt kĩ năng bài tương ứng
        :param nBoard: Bàn cờ (board.Board)
        :param indexs: Danh sách các tọa độ (list(tuple(int, int))
        :param playTeam: Đội đang trong lượt
        :return: Kết quả (str)
        """
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
                    result.append(copy.copy(effect).active_effect(nBoard, indexs, 3, options = self.__options, playTeam = playTeam, histLog = histLog))
                    effect.unactive_effect()
                except:
                    result.append(ef.STATUS[1])
            if ef.STATUS[3] in result:
                result[result.index(ef.STATUS[3])] = 'Casted'
            return result

        def MultiEffects():
            pass

        try:
            result = locals()[self.__skillCard](self.__effects, nBoard, indexs)
        except:
            result = 'Fail'
        return result

class CardArea:
    """
    Lớp "Khu vực bài phép"
    """
    def __init__(self, height, width, offsetHeight, offsetWidth, lImg):
        """
        Hàm khởi tộ
        :param height: Chiều cao (int)
        :param width: Chiều rộng (int)
        :param offsetHeight: Khoảng các từ mép trên cửa sổ hiển thị đến bàn cờ (int)
        :param offsetWidth: Khoảng các từ mép bên cửa sổ hiển thị đến bàn cờ (int)
        :param lImg: Danh sách hình ảnh (list(pygame.image))
        """
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
        """
        Hàm in các lá bài lên cửa sổ hiển thị
        :param win: Cửa sổ hiển thị (pygame.display)
        :param font: Font chữ (font.Font)
        :param pos: Vị trí lá bài được hiển thị (tuple(int, int))
        :param nPlayer: Danh sách người chơi (list(player.Player))
        :return: None
        """
        listCard = nPlayer.get_cards()
        picking = nPlayer.get_picking()
        interval = self.__Height / 3
        for cell in self.__cellLayers:
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
        """
        Hàm xác định lá bài được chọn
        :param pos: vị chí con trỏ chuột (tuple(int, int))
        :return: Vị trí lá bài trong danh sách bài của người chơi (int)
        """
        for i in range(3):
            if self.__cellLayers[i].is_mouse_hovering(pos):
                return i
        return None