import random

import pygame
import chess
import init
import cell

class Board:
    def __init__(self, x, y, width, pTeam, evironment, lImg):
        self.__x = x
        self.__y = y
        self.__width = width
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
        self.__cellType = [lImg[evironment]]
        interval = self.__width / 8
        self.__CellLayer = [[]*8]*8
        for i in range(8):
            for j in range(8):
                self.__CellLayer[i][j] = Cell(i * interval + self.__x, j * interval + self.__y, self.__cellType["normal"])
        self.__readableMap = [[]*8]*8
        for i in range(8):
            for j in range(8):
                try:
                    self.__readableMap[i][j] = self.__OjectLayer[(i, j)].convert_to_readable()
                except:
                    self.__readableMap[i][j] = ' '

    def draw(self, win):
        for row in range(8):
            for col in range(8):
                self.__CellLayer[row][col].draw(win)
                self.__OjectLayer[row][col].draw(win, self.__CellLayer[row][col].get_pos())

    def find_Cell(self, pos):
        interval = self.__width / 8
        y, x = pos
        row = (y - self.__y) // interval
        col = (x - self.__x) // interval
        return (int(row), int(col))

    def check_Team(self, index, teamCheck):
        try:
            if self.__OjectLayer(index).get_team() == teamCheck:
                return True
            else:
                return False
        except:
            return False

    def select_Chess(self, pos, turn):
        playingTeam = 'b'
        if moves % 2 == 0:
            playingTeam = 'w'
        index = self.find_Cell(pos)
        if self.check_Team(index, playingTeam):
            self.__OjectLayer(index).get_moves(self.__OjectLayer, self.__readableMap, index)

    def deseclect(self):
        for row in range(8):
            for col in range(8):
                if self.__readableMap[row][col] == 'x':
                    self.__readableMap[row][col] = ' '
                    try:
                        self.__OjectLayer[(row, col)].set_killable(False)
                    except:
                        pass

    def convert_to_readable(self):
        new_map = [[] * 8] * 8
        for i in range(8):
            for j in range(8):
                try:
                    self.__readableMap[i][j] = self.__OjectLayer[(i, j)].convert_to_readable()
                except:
                    self.__readableMap[i][j] = ' '
        return new_map

    def select_Move(self, pos, new_pos, phase):
        index0 = self.find_Cell(pos)
        index1 = self.find_Cell(new_pos)
        if self.__readableMap[index1[0]][index1[1]] == 'x':
            self.__OjectLayer[index0[0]][index0[1]].delete_effect('First Move')
            self.__OjectLayer[index1[0]][index1[1]] = self.__OjectLayer[index0[0]][index0[1]]
            self.__OjectLayer[index0[0]][index0[1]] = None
        self.__readableMap = self.convert_to_readable()
        self.deseclect()