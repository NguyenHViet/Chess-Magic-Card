import pygame

class Effect:
    def __init__(self, name, value = 1, stack = 1, turns = 1, phase = 0, actived = False):
        self.__name = name
        self.__value = value
        self.__stack = stack
        self.__turns = turns
        self.__phase = phase
        self.__actived = actived
        self.__describe = ''
        pass

    def get_name(self):
        return  self.__name

    def is_over(self):
        if (self.__stack <= 0 or self.__turns <= 0) and '!' not in self.__name:
            return True
        else:
            return False

    def unactive_effect(self):
        self.__actived = False

    def active_effect(self, nBoard, indexs, phase, **options):
        def IncreaseSpeed(nBoard, indexs, phase, value, options):
            try:
                index = indexs[0]
                oBoard = nBoard.getoBoard()
                rBoard = nBoard.getrBoard()
                oBoard[(index[1], index[0])].change_speed(value)
                return 'Effected'
            except:
                return 'Fail'

        def PushChess(nBoard, indexs, phase, value, options):
            oBoard = nBoard.getoBoard()
            rBoard = nBoard.getrBoard()
            try:
                index = indexs[0]
                rBoard[index[0]][index[1]] += ':'

                moveRange = []
                directions = options['directions']
                for i in range(value + 1):
                    if 'Ahead Left' in directions:
                        moveRange.append([index[0] + oBoard[(index[1], index[0])].get_direction()*i,
                                          index[1] - oBoard[(index[1], index[0])].get_direction()*i])
                    if 'Ahead' in directions:
                        moveRange.append([index[0] + oBoard[(index[1], index[0])].get_direction()*i,
                                          index[1]])
                    if 'Ahead Right' in directions:
                        moveRange.append([index[0] + oBoard[(index[1], index[0])].get_direction() * i,
                                          index[1] + oBoard[(index[1], index[0])].get_direction() * i])

                for positions in moveRange:
                    if chess.on_board(positions) and rBoard[positions[0]][positions[1]] == ' ':
                        rBoard[positions[0]][positions[1]] = 'x'
                        oBoard[(positions[1], positions[0])].set_killable(options['killable'])
                if len(indexs) == 2:
                    new_index = indexs[1]
                    if nBoard.select_Move(index, new_index) == 1:
                        return 'Effected'
                    else:
                        return 'Fail'
            except:
                return 'Fail'
            return 'Success'

        if phase == self.__phase and not self.__actived and '!' not in self.__name:
            func = locals()[self.__name](nBoard, indexs, phase, self.__value, options)
            if func != 'Fail':
                self.__actived = True
                return func
        else:
            return 'Fail'

    def triggered_effect(self):
        self.__stack -= 1

