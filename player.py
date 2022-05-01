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
            self.__cards.append(random.choice(copy.copy(deck)))

    def draw_cards(self, deck):
        self.__cards = random.choices(copy.copy(deck), k = 3)

    def pick_card(self, index):
        self.__picking = index
        return self.__cards[index].get_selected_require()

    def decelect(self):
        self.__picking = -1

    def play_card(self, oBoard, rBoard, indexs):
        try:
            self.__cards[self.__picking].play_card(oBoard, rBoard, indexs)
        except:
            pass

    def get_cards(self):
        return self.__cards

    def get_picking(self):
        return self.__picking

    def update(self, phase, deck, timeBonus, addableTime):
        if phase == chess.PHASE['Start']:
            self.__actions = 3
            self.draw_cards(deck)
            print(self.__cards)
            self.__timeBonus = timeBonus
        elif phase == chess.PHASE['End']:
            if addableTime:
                self.__time += self.__timeBonus
                self.__timeBonus = 0
