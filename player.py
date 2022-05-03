import card
import cell
import copy
import random

import chess


class Player:
    def __init__(self, name, team, time = 120):
        self.__name = name
        self.__team = team
        self.__actions = 3
        self.__cards = []
        self.__picking = -1
        self.__time = time
        self.__timeBonus = 0


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
        self.__picking = -1

    def play_card(self, nBoard, indexs):
        try:
            result = self.__cards[self.__picking].play_card(nBoard, indexs, self.__team)
            if result == 'Casted':
                self.__actions -= self.__cards[self.__picking].get_cost()
                self.__cards.pop(self.__picking)
            return result
        except:
            return 'Fail'

    def get_cards(self):
        return self.__cards

    def get_picking(self):
        return self.__picking

    def update(self, phase, deck, timeBonus, addableTime):
        nPhase = phase
        if phase == chess.PHASE['Start']:
            self.__actions = 3
            self.draw_cards(deck)
            self.__timeBonus = timeBonus
        elif self.__actions <= 0:
            nPhase = chess.PHASE['End']
        elif phase == chess.PHASE['End']:
            if addableTime:
                self.__time += self.__timeBonus
                self.__timeBonus = 0
        return nPhase