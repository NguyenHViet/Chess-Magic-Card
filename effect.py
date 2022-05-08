import pygame
import chess

STATUS = {
    0:'Not Effected', 1:'Fail', 2:'Success', 3:'Effected'
}

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

    def is_over(self, phase):
        self.unactive_effect()
        if phase == chess.PHASE['End']:
            self.__turns -= 1
        if (self.__stack <= 0 or self.__turns <= 0) and '!' not in self.__name:
            return True
        else:
            return False

    def unactive_effect(self):
        self.__actived = False

    def active_effect(self, nBoard, indexs, phase = 0, **options):
        try:
            Options = options['options']
            options.pop('options')
            Options.update(options)
        except:
            Options = []

        # Chess Effect
        def IncreaseSpeed(nBoard, indexs, phase, value, options):
            if phase != self.__phase:
                return STATUS[0]
            try:
                index = indexs[0]
                oBoard = nBoard.getoBoard()
                oBoard[(index[1], index[0])].change_speed(value)
                return STATUS[3]
            except:
                return STATUS[1]

        def Unselectable(nBoard, indexs, phase, value, options):
            return STATUS[1]

        # Card Effect
        def PushChess(nBoard, indexs, phase, value, options):
            if phase != self.__phase:
                return STATUS[0]
            oBoard = nBoard.getoBoard()
            rBoard = nBoard.getrBoard()
            try:
                index = indexs[0]
                if not nBoard.select_Chess(index, phase, options['playTeam'], False):
                    return STATUS[1]
                moveRange = []
                directions = options['directions']
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

                for positions in moveRange:
                    if chess.on_board(positions) and rBoard[positions[0]][positions[1]] == ' ' and '!' not in rBoard[positions[0]][positions[1]]:
                        rBoard[positions[0]][positions[1]] = 'x'
                    else:
                        try:
                            oBoard[(positions[1], positions[0])].set_killable(nBoard, positions, phase, options['killable'])
                            if oBoard[(positions[1], positions[0])].get_killable() and oBoard[(positions[1], positions[0])].get_team() != oBoard[(index[1], index[0])].get_team():
                                rBoard[positions[0]][positions[1]] += 'x'
                                break
                        except:
                            pass
                if len(indexs) == 2:
                    new_index = indexs[1]
                    if nBoard.select_Move(index, new_index, triggeredEffect = False):
                        self.unactive_effect()
                        return STATUS[3]
                    else:
                        return STATUS[1]
            except:
                return STATUS[1]
            return STATUS[2]

        if not self.__actived and self.__stack > 0:
            func = locals()[self.__name](nBoard, indexs, phase, self.__value, Options)
            if func == STATUS[3]:
                self.__actived = True
            return func
        else:
            return STATUS[0]

    def triggered_effect(self):
        self.__stack -= 1
        self.unactive_effect()

