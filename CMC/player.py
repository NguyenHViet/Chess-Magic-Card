import copy
import random
import math
import time

import CMC.chess as chess
import CMC.init as init

class Player:
    """
    Lớp "Người Chơi"
    """
    def __init__(self, name, team, time = 120, timeBonus = 0, totalActions = 20):
        """
        Hàm khởi tạo
        :param name: Tên người chơi (str)
        :param team: Tên đội (str)
        :param time: Thời gian đầu trận (int)
        :param timeBonus: Thời gian thưởng thêm trong lượt (int)
        :param totalActions: Tổng lượng năng lượng hồi trong trận đấu (int)
        """
        self.__name = name
        self.__team = team
        self.__totalActions = totalActions
        self.__actions = 0
        self.__cards = []
        self.__picking = None
        self.__totalTime = time
        self.__time = self.__totalTime
        self.__timeBonus = timeBonus
        self.__reRoll = False

    def set_time(self, new_time):
        """
        Gán thời gian mới
        :param new_time: Thời gian mới (int)
        :return: None
        """
        self.__time = new_time

    def get_picking(self):
        """
        Lấy quân bài đang được chọn
        :return: Chỉ số quân bài đang được chọn (int)
        """
        return self.__picking

    def draw_card(self, deck):
        """
        Nhận thêm lá bài
        :param deck: Bộ bài (list(card.Card))
        :return: None
        """
        if len(self.__cards) < 3:
            self.__cards.append(copy.copy(random.choice(deck)))

    def redraw_card(self, index):
        """
        Đổi lại lá bài
        :param index: Vị trí lá bài cần đổi (int)
        :return: None
        """
        if not self.__reRoll:
            self.__cards[index['param']] = copy.copy(random.choice(init.DECK))
            self.__reRoll = True

    def draw_cards(self, deck):
        """
        Đổi lại toàn bộ lá bài
        :param deck: Bộ bài (list(card.Card))
        :return: None
        """
        self.__cards.clear()
        random.shuffle(deck)
        for i in range(3):
            self.__cards.append(copy.copy(deck[i]))

    def pick_card(self, index):
        """
        Chọn lá bài và nhận số lượng đối tượng cần thiết để dùng bài phép
        :param index: Vị trí lá bài
        :return: Số lượng đối tượng cần thiết (int)
        """
        if self.__cards[index].get_cost() <= self.__actions:
            self.__picking = index
            return self.__cards[index].get_selected_require()
        else:
            return -1

    def decelect(self):
        """
        Hủy chọn bài
        :return: None
        """
        self.__picking = None

    def play_card(self, nBoard, indexs):
        """
        Sử dụng bài phép
        :param nBoard: Bàn cờ (board.Board)
        :param indexs: Danh sách vị trí các đối tượng được chọn (tuple(int, int))
        :return: Kết quả dùng bài phép (str)
        """
        try:
            result = self.__cards[self.__picking].play_card(nBoard, indexs, self.__team)
            if 'Casted' in result:
                self.__actions -= self.__cards[self.__picking].get_cost()
                self.__cards.pop(self.__picking)
            return result
        except:
            return 'Fail'

    def get_cards(self):
        """
        Lấy danh sách các lá bài người chơi sở hữu
        :return: Danh sách các lá bài (list(card.Card))
        """
        return self.__cards

    def get_picking(self):
        """
        Lấy vị trí lá bài đang được chọn
        :return: Vị trí lá bài đang được chọn (int)
        """
        return self.__picking

    def get_time(self):
        """
        Lấy thời gian còn lại của người chơi
        :return: Thời gian còn lại (int)
        """
        return self.__time

    def get_action(self):
        """
        Lấy số lượng năng lượng còn lại của người chơi
        :return: Số lượng năng lượng còn lại của người chơi (int)
        """
        return self.__actions

    def get_totalAction(self):
        """
        Lấy tổng số năng lượng có thể nhận trong trận đấu
        :return: Tổng số năng lượng có thể nhận (int)
        """
        return self.__totalActions

    def update(self, phase, deck, addableTime, startTurnTime):
        """
        Cập nhập trạng thái người chơi
        :param phase: Giai đoạn của lượt hiện tại (int)
        :param deck: Bộ bài (list(card.Card))
        :param addableTime: Cộng dồn thời gian (bool)
        :param startTurnTime: Thời gian khi bắt đầu lượt (time.time())
        :return: Giai doạn của lượt hiện tại (int)
        """
        nowTime = math.floor(time.time())
        timing = nowTime - startTurnTime
        nPhase = phase
        if phase == chess.PHASE['Start']:
            self.__reRoll = False
            self.__time = self.__totalTime + self.__timeBonus
            if self.__actions < 5 and self.__totalActions > 0:
                self.__actions += 1
                self.__totalActions -= 1
            self.draw_card(deck)
        if self.__actions <= 0:
            nPhase = chess.PHASE['End']
        if phase == chess.PHASE['End']:
            if addableTime or self.__time - timing <= self.__totalTime:
                self.__totalTime = self.__time - timing
                self.__time = self.__totalTime
        return nPhase