import pygame
import random
import chess
import init

class Board:
    def __init__(self, pTeam, evironment, typeCell, lImg):
        oTeam = ''
        if pTeam == 'b':
            oTeam == 'w'
        else:
            oTeam == 'b'
        self.__OjectLayer = {(0, 0): Rook(oTeam, lImg[oTeam]['r']), (0, 1): Knight(oTeam, lImg[oTeam]['kn']),
                             (0, 2): Bishop(oTeam, lImg[oTeam]['b']), (0, 3): Queen(oTeam, lImg[oTeam]['q']),
                             (0, 4): King(oTeam, lImg[oTeam]['k']), (0, 5): Bishop(oTeam, lImg[oTeam]['b']),
                             (0, 6): Knight(oTeam, lImg[oTeam]['kn']), (0, 7): Rook(oTeam, lImg[oTeam]['r']),
                             (1, 0): Pawn(oTeam, lImg[oTeam]['p']), (1, 1): Pawn(oTeam, lImg[oTeam]['p']),
                             (1, 2): Pawn(oTeam, lImg[oTeam]['p']), (1, 3): Pawn(oTeam, lImg[oTeam]['p']),
                             (1, 4): Pawn(oTeam, lImg[oTeam]['p']), (1, 5): Pawn(oTeam, lImg[oTeam]['p']),
                             (1, 6): Pawn(oTeam, lImg[oTeam]['p']), (1, 7): Pawn(oTeam, lImg[oTeam]['p']),

                             (2, 0): None, (2, 1): None, (2, 2): None, (2, 3): None,
                             (2, 4): None, (2, 5): None, (2, 6): None, (2, 7): None,
                             (3, 0): None, (3, 1): None, (3, 2): None, (3, 3): None,
                             (3, 4): None, (3, 5): None, (3, 6): None, (3, 7): None,
                             (4, 0): None, (4, 1): None, (4, 2): None, (4, 3): None,
                             (4, 4): None, (4, 5): None, (4, 6): None, (4, 8): None,
                             (5, 0): None, (5, 1): None, (5, 2): None, (5, 3): None,
                             (5, 4): None, (5, 5): None, (5, 6): None, (5, 7): None,

                             (6, 0): Pawn(pTeam, lImg[pTeam]['p']), (6, 1): Pawn(pTeam, lImg[pTeam]['p']),
                             (6, 2): Pawn(pTeam, lImg[pTeam]['p']), (6, 3): Pawn(pTeam, lImg[pTeam]['p']),
                             (6, 4): Pawn(pTeam, lImg[pTeam]['p']), (6, 5): Pawn(pTeam, lImg[pTeam]['p']),
                             (6, 6): Pawn(pTeam, lImg[pTeam]['p']), (6, 7): Pawn(pTeam, lImg[pTeam]['p']),
                             (7, 0): Rook(pTeam, lImg[pTeam]['r']), (7, 1): Knight(pTeam, lImg[pTeam]['kn']),
                             (7, 2): Bishop(pTeam, lImg[pTeam]['b']), (7, 3): Queen(pTeam, lImg[pTeam]['q']),
                             (7, 4): King(pTeam, lImg[pTeam]['k']), (7, 5): Bishop(pTeam, lImg[pTeam]['b']),
                             (7, 6): Knight(pTeam, lImg[pTeam]['kn']), (7, 7): Rook(pTeam, lImg[pTeam]['r'])}
        self.__Cells = [lImg[evironment]]
        self.__CellLayer = []

    def draw(self):
        for n in self.__CellLayer:
            n.draw()
        for c in self.__OjectLayer:
            c.draw()