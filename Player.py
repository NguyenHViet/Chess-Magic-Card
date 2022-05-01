import card
import cell
import copy
import random

class Player:
    def __init__(self, name, team):
        self.__name = name
        self.__team = team
        self.__actions = 3
        self.__cards = []
        self.__handLayer = [cell.Cell()]


    def draw_card(self, deck):
        if len(self.__cards) < 3:
            self.__cards.append(random.choice(copy.copy(deck)))

    def draw_cards(self, deck):
        self.__cards == random.choices(copy.copy(deck), k = 3)

    def pick_card(self, height, pos, phase):
        interval = height / 3
        pos[0]