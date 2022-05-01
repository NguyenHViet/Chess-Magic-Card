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

    def active_effect(self, oBoard, rBoard, index, phase):
        def IncreaseSpeed(oBoard, rBoard, index, phase, value):
            oBoard[(index[0], index[1])].change_speed(value)

        if phase == self.__phase and not self.__actived:
            locals()[self.__name](oBoard, rBoard, index, phase, self.__value)
            self.__actived = True

    def triggered_effect(self):
        self.__stack -= 1

