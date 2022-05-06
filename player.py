import card
import cell
import copy
import random
import pygame
import math
import time

import chess


class Player:
    def __init__(self, name, team, time = 120, timeBonus = 0):
        self.__name = name
        self.__team = team
        self.__actions = 0
        self.__cards = []
        self.__picking = None
        self.__totalTime = time
        self.__time = self.__totalTime
        self.__timeBonus = timeBonus

    def set_time(self, new_time):
        self.__time = new_time

    def get_picking(self):
        return self.__picking

    def draw_card(self, deck):
        if len(self.__cards) < 3:
            self.__cards.append(copy.copy(random.choice(deck)))

    def draw_cards(self, deck):
        self.__cards.clear()
        for i in range(3):
            new_card = random.choice(deck)
            self.__cards.append(copy.copy(new_card))

    def pick_card(self, index):
        if self.__cards[index].get_cost() <= self.__actions:
            self.__picking = index
            return self.__cards[index].get_selected_require()
        else:
            return -1

    def decelect(self):
        self.__picking = None

    def play_card(self, nBoard, indexs):
        try:
            result = self.__cards[self.__picking].play_card(nBoard, indexs, self.__team)
            if 'Casted' in result:
                self.__actions -= self.__cards[self.__picking].get_cost()
                self.__cards.pop(self.__picking)
            return result
        except:
            return 'Fail'

    def get_cards(self):
        return self.__cards

    def get_picking(self):
        return self.__picking

    def get_time(self):
        return self.__time

    def get_action(self):
        return self.__actions

    def update(self, phase, deck, addableTime, startTurnTime):
        nowTime = math.floor(time.time())
        timing = nowTime - startTurnTime
        nPhase = phase
        if phase == chess.PHASE['Start']:
            self.__time = self.__totalTime + self.__timeBonus
            if self.__actions < 3:
                self.__actions += 1
            self.draw_cards(deck)
        elif self.__actions <= 0:
            nPhase = chess.PHASE['End']
        elif phase == chess.PHASE['End']:
            if addableTime:
                self.__totalTime = self.__time - timing
                self.__time = self.__totalTime
            elif self.__time - timing <= self.__totalTime:
                self.__totalTime = self.__time - timing
                self.__time = self.__totalTime
        return nPhase