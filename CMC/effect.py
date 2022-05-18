import CMC.chess as chess

STATUS = {
    0:'Not Effected', 1:'Fail', 2:'Success', 3:'Effected'
}

class Effect:
    """
    Lớp "Hiệu Ứng"
    """
    def __init__(self, name, value = 1, stack = 1, turns = 1, phase = 0, actived = False):
        """
        Hàm khởi tạo
        :param name: Tên hiệu ứng (str)
        :param value: Giá trị được sử dụng (int)
        :param stack: Tích lũy của hiệu ứng (int)
        :param turns: Số lượt hiệu ứng tồn tại (int)
        :param phase: Giai đoạn hiệu ứng được áp dụng trong lượt (int)
        :param actived: Trạng thái kích hoạt hiệu ứng (bool)
        """
        self.__name = name
        self.__value = value
        self.__stack = stack
        self.__turns = turns
        self.__phase = phase
        self.__actived = actived
        self.__describe = ''
        pass

    def get_name(self):
        """
        Lấy tên hiệu ứng
        :return: Tên hiệu ứng (str)
        """
        return  self.__name

    def is_over(self, phase):
        """
        Kiểm tra hiệu ứng đã kết thúc
        :param phase: Giai đoạn của lượt hiện tại
        :return: Kết quả (bool)
        """
        if phase == chess.PHASE['End']:
            self.__turns -= 1
        if (self.__stack == 0 or self.__turns == 0) and '!' not in self.__name:
            return True
        else:
            return False

    def unactive_effect(self):
        """
        Hủy kích hoạt hiệu ứng
        :return: None
        """
        self.__actived = False

    def active_effect(self, nBoard, indexs, phase = 0, **options):
        """
        Kích hoạt hiệu ứng
        :param nBoard: Bàn cờ (board.Board)
        :param indexs: Tọa độ những ô được chọn trên bàn cờ (list(tuple(int, int)))
        :param phase: Giai đoạn của lượt hiện tại (int)
        :param options: Các giá trị tùy chọn
        :return: Kết quả hiệu ứng
        """
        try:
            Options = options['options']
            options.pop('options')
            Options.update(options)
        except:
            Options = []

        # Chess Effect
        def IncreaseSpeed(nBoard, indexs, phase, value, options):
            """
            Tăng tốc độ cho quân cờ được chọn
            :param nBoard: Bàn cờ (board.Board)
            :param indexs: Tọa độ ô được chọn (list(tuple(int, int)))
            :param phase: Giai đoạn của lượt hiện tại
            :param value: Lượng tốc độ được tăng (int)
            :param options: Các giá trị tùy chọn
            :return: Kết quả hiệu ứng (str)
            """
            if phase != self.__phase:
                return STATUS[0]
            try:
                index = indexs[0]
                oBoard = nBoard.getoBoard()
                oBoard[(index[1], index[0])].change_speed(value)
                return STATUS[3]
            except:
                return STATUS[0]

        def Unselectable(nBoard, indexs, phase, value, options):
            """
            Quân cờ không thể được chọn
            :param nBoard: Bàn cờ (board.Board)
            :param indexs: Tọa độ ô được chọn (list(tuple(int, int)))
            :param phase: Giai đoạn của lượt hiện tại
            :param value: Lượng tốc độ được tăng (int)
            :param options: Các giá trị tùy chọn
            :return: Kết quả hiệu ứng (str)
            """
            if phase in self.__phase:
                return STATUS[1]
            else:
                return STATUS[0]

        def Unmove(nBoard, indexs, phase, value, options):
            """
            Quân cờ vẫn chưa di chuyển lần nào trong trận đấu
            :param nBoard: Bàn cờ (board.Board)
            :param indexs: Tọa độ ô được chọn (list(tuple(int, int)))
            :param phase: Giai đoạn của lượt hiện tại
            :param value: Lượng tốc độ được tăng (int)
            :param options: Các giá trị tùy chọn
            :return: Kết quả hiệu ứng (str)
            """
            if phase in self.__phase:
                return STATUS[2]
            else:
                return STATUS[0]

        # Card Effect


        def PushChess(nBoard, indexs, phase, value, options):
            """
            Tăng thêm khả năng di chuyển cho quân cờ được chọn
            :param nBoard: Bàn cờ (board.Board)
            :param indexs: Tọa độ ô được chọn (list(tuple(int, int)))
            :param phase: Giai đoạn của lượt hiện tại
            :param value: Lượng tốc độ được tăng (int)
            :param options: Các giá trị tùy chọn
            :return: Kết quả hiệu ứng (str)
            """
            if phase != self.__phase:
                return STATUS[0]
            oBoard = nBoard.getoBoard()
            rBoard = nBoard.getrBoard()
            try:
                index = indexs[0]
                result = nBoard.select_Chess(index, phase, options['playTeam'], False)
                if not result[0]:
                    return STATUS[1]
                moveRange = []
                directions = options['directions']

                if 'Around' in directions:
                    for i in range(-value, value + 1):
                        for j in range(-value, value + 1):
                            if i == 0 and j == 0:
                                continue
                            moveRange.append([index[0] + i, index[1] + j])
                else:
                    for i in range(1, value + 1):
                        if 'Ahead Left' in directions:
                            moveRange.append([index[0] + oBoard[(index[1], index[0])].get_direction()*i, index[1] - i])
                        if 'Ahead' in directions:
                            moveRange.append([index[0] + oBoard[(index[1], index[0])].get_direction()*i, index[1]])
                        if 'Ahead Right' in directions:
                            moveRange.append([index[0] + oBoard[(index[1], index[0])].get_direction() * i, index[1] + i])
                        if 'Right' in directions:
                            moveRange.append([index[0], index[1] + i])
                        if 'Back Right' in directions:
                            moveRange.append([index[0] - oBoard[(index[1], index[0])].get_direction() * i, index[1] + i])
                        if 'Back' in directions:
                            moveRange.append([index[0] - oBoard[(index[1], index[0])].get_direction() * i, index[1]])
                        if 'Back Left' in directions:
                            moveRange.append([index[0] - oBoard[(index[1], index[0])].get_direction() * i, index[1] - i])
                        if 'Left' in directions:
                            moveRange.append([index[0], index[1] - i])

                if options['playTeam'] == 'b':
                    target = ['w']
                else:
                    target = ['b']

                try:
                    if not options['enemy']:
                        target = [options['playTeam']]
                except:
                    target = ['b', 'w']

                try:
                    swap = options['swap']
                except:
                    swap = False

                for positions in moveRange:
                    if chess.on_board(positions) and oBoard[(positions[1], positions[0])] == None and '!' not in rBoard[positions[0]][positions[1]] and not swap:
                        rBoard[positions[0]][positions[1]] += 'x'
                    else:
                        try:
                            oBoard[(positions[1], positions[0])].set_killable(nBoard, positions, phase, options['killable'])
                            MagicResist = oBoard[(positions[1], positions[0])].active_effects(nBoard, positions, phase)
                            if swap:
                                try:
                                    if oBoard[(positions[1], positions[0])].get_team() in target and 'Fail' not in MagicResist:
                                        rBoard[positions[0]][positions[1]] += 'x'
                                except:
                                    pass
                            if oBoard[(positions[1], positions[0])].get_killable() and options['playTeam'] != oBoard[(positions[1], positions[0])].get_team() and 'Fail' not in MagicResist:
                                rBoard[positions[0]][positions[1]] += 'x'
                                break
                        except:
                            pass

                if len(indexs) == 2:
                    new_index = indexs[1]
                    if nBoard.select_Move(index, new_index, triggeredEffect = False, swap = swap, HistLog=options['HistLog']):
                        self.unactive_effect()
                        return STATUS[3]
                    else:
                        return STATUS[1]
            except:
                return STATUS[1]
            return STATUS[2]

        if not self.__actived and self.__stack > 0 or self.__stack == -1:
            func = locals()[self.__name](nBoard, indexs, phase, self.__value, Options)
            if func == STATUS[3]:
                self.__actived = True
            return func
        else:
            return STATUS[0]

    def triggered_effect(self, phase = 2):
        """
        Giảm tích lũy của hiệu ứng
        :param phase: Giai đoạn của lượt hiện tại
        :return: None
        """
        if phase == self.__phase:
            if self.__stack > 0:
                self.__stack -= 1
            self.unactive_effect()

