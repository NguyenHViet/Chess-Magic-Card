import card
import cell
import copy
import random
import pygame
import math
import time

import chess
import init


class Player:
    def __init__(self, name, team, time = 120, timeBonus = 0, totalActions = 15):
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
        self.__time = new_time

    def get_picking(self):
        return self.__picking

    def draw_card(self, deck):
        if len(self.__cards) < 3:
            self.__cards.append(copy.copy(random.choice(deck)))

    def redraw_card(self, index):
        if not self.__reRoll:
            self.__cards[index] = copy.copy(random.choice(init.DECK))
            self.__reRoll = True

    def draw_cards(self, deck):
        self.__cards.clear()
        random.shuffle(deck)
        for i in range(3):
            self.__cards.append(copy.copy(deck[i]))

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

    def get_totalAction(self):
        return self.__totalActions

    def update(self, phase, deck, addableTime, startTurnTime):
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