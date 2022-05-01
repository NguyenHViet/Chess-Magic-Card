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
        oTeam = 'b'
        if pTeam == 'b':
            oTeam == 'w'
        else:
            oTeam == 'b'
        # Tạo phần layer các thực thể trên bàn cờ
        self.__OjectLayer = {(0, 0): chess.Rook(oTeam, 'downward', lImg[oTeam]['r']), (1, 0): chess.Knight(oTeam, 'downward', lImg[oTeam]['kn']),
                             (2, 0): chess.Bishop(oTeam, 'downward', lImg[oTeam]['b']), (3, 0): chess.Queen(oTeam, 'downward', lImg[oTeam]['q']),
                             (4, 0): chess.King(oTeam, 'downward', lImg[oTeam]['k']), (5, 0): chess.Bishop(oTeam, 'downward', lImg[oTeam]['b']),
                             (6, 0): chess.Knight(oTeam, 'downward', lImg[oTeam]['kn']), (7, 0): chess.Rook(oTeam, 'downward', lImg[oTeam]['r']),
                             (0, 1): chess.Pawn(oTeam, 'downward', lImg[oTeam]['p']), (1, 1): chess.Pawn(oTeam, 'downward', lImg[oTeam]['p']),
                             (2, 1): chess.Pawn(oTeam, 'downward', lImg[oTeam]['p']), (3, 1): chess.Pawn(oTeam, 'downward', lImg[oTeam]['p']),
                             (4, 1): chess.Pawn(oTeam, 'downward', lImg[oTeam]['p']), (5, 1): chess.Pawn(oTeam, 'downward', lImg[oTeam]['p']),
                             (6, 1): chess.Pawn(oTeam, 'downward', lImg[oTeam]['p']), (7, 1): chess.Pawn(oTeam, 'downward', lImg[oTeam]['p']),

                             (0, 2): None, (1, 2): None, (2, 2): None, (3, 2): None,
                             (4, 2): None, (5, 2): None, (6, 2): None, (7, 2): None,
                             (0, 3): None, (1, 3): None, (2, 3): None, (3, 3): None,
                             (4, 3): None, (5, 3): None, (6, 3): None, (7, 3): None,
                             (0, 4): None, (1, 4): None, (2, 4): None, (3, 4): None,
                             (4, 4): None, (5, 4): None, (6, 4): None, (7, 4): None,
                             (0, 5): None, (1, 5): None, (2, 5): None, (3, 5): None,
                             (4, 5): None, (5, 5): None, (6, 5): None, (7, 5): None,

                             (0, 6): chess.Pawn(pTeam, 'upward', lImg[pTeam]['p']), (1, 6): chess.Pawn(pTeam, 'upward', lImg[pTeam]['p']),
                             (2, 6): chess.Pawn(pTeam, 'upward', lImg[pTeam]['p']), (3, 6): chess.Pawn(pTeam, 'upward', lImg[pTeam]['p']),
                             (4, 6): chess.Pawn(pTeam, 'upward', lImg[pTeam]['p']), (5, 6): chess.Pawn(pTeam, 'upward', lImg[pTeam]['p']),
                             (6, 6): chess.Pawn(pTeam, 'upward', lImg[pTeam]['p']), (7, 6): chess.Pawn(pTeam, 'upward', lImg[pTeam]['p']),
                             (0, 7): chess.Rook(pTeam, 'upward', lImg[pTeam]['r']), (1, 7): chess.Knight(pTeam, 'upward', lImg[pTeam]['kn']),
                             (2, 7): chess.Bishop(pTeam, 'upward', lImg[pTeam]['b']), (3, 7): chess.Queen(pTeam, 'upward', lImg[pTeam]['q']),
                             (4, 7): chess.King(pTeam, 'upward', lImg[pTeam]['k']), (5, 7): chess.Bishop(pTeam, 'upward', lImg[pTeam]['b']),
                             (6, 7): chess.Knight(pTeam, 'upward', lImg[pTeam]['kn']), (7, 7): chess.Rook(pTeam, 'upward', lImg[pTeam]['r'])}
        self.__GEI = lImg['GEI']

        # Tạo phần layer các ô trên bàn cờ
        interval = self.__width / 8
        self.__CellLayer = []
        for x in range(8):
            self.__CellLayer.append([])
            for y in range(8):
                self.__CellLayer[x].append(cell.Cell((x * interval) + self.__y, (y * interval) + self.__x, self.__GEI["Normal"]))
        # Tạo phần readable để làm input cho các hàm khác
        self.__readableMap = [[' ' for i in range (8)] for i in range(8)]
        self.__readableMap = self.convert_to_readable()

    def draw(self, win):
        interval = self.__width / 8
        for row in range(8):
            for col in range(8):
                self.__CellLayer[row][col].draw(win, interval, interval)
                if (row+col) % 2 == 0:
                    win.blit(self.__GEI['Darken'] ,(self.__CellLayer[row][col].get_x(), self.__CellLayer[row][col].get_y()))
                if self.__readableMap[col][row] == 'x':
                    win.blit(self.__GEI['Move'] ,(self.__CellLayer[row][col].get_x(), self.__CellLayer[row][col].get_y()))
                elif (self.__readableMap[col][row])[-1] == ':':
                    win.blit(self.__GEI['Choice'],
                             (self.__CellLayer[row][col].get_x(), self.__CellLayer[row][col].get_y()))
                if not self.__OjectLayer[(row, col)] == None:
                    self.__OjectLayer[(row, col)].draw(win, self.__CellLayer[row][col].get_pos(), interval)

    def printMap(self):
        for i in range(8):
            print(" ".join(["{:^8}" for j in range(8)]).format(*self.__readableMap[i]))
        return True

    def count_on_rMap(self, object):
        count = 0
        for item in self.__readableMap:
            if object in item:
                count += 1
        return count

    def find_Cell(self, pos):
        interval = self.__width / 8
        y, x = pos
        row = (x - self.__x) // interval
        col = (y - self.__y) // interval
        return int(row), int(col)

    def check_Team(self, index, teamCheck):
        try:
            if self.__OjectLayer[index].get_team() == teamCheck:
                return True
            else:
                return False
        except:
            return False

    def select_Chess(self, pos, phase, playingTeam = 'b'):
        index = self.find_Cell(pos)
        y, x = index
        if self.check_Team((x, y), playingTeam):
            print("Team turn:", playingTeam)
            self.__OjectLayer[(x, y)].active_effects(self.__OjectLayer, self.__readableMap, index, phase)
            self.__OjectLayer[(x, y)].get_moves(self.__OjectLayer, self.__readableMap, index)
            print("Chọn thành công quân cờ:", self.__readableMap[y][x], (y, x))
            self.printMap()
            return True
        else:
            print("Không thể chọn")
            return False

    def deseclect(self):
        self.__readableMap = [[' ' for i in range(8)] for i in range(8)]
        for i in range(8):
            for j in range(8):
                try:
                    self.__readableMap[i][j] = self.__OjectLayer[(j, i)].convert_to_readable()
                    self.__OjectLayer[(j, i)].set_killable(False)
                except:
                    self.__readableMap[i][j] = ' '

    def convert_to_readable(self):
        new_map = self.__readableMap
        for i in range(8):
            for j in range(8):
                try:
                    new_map[i][j] = self.__OjectLayer[(j, i)].convert_to_readable()
                except:
                    new_map[i][j] = ' '
        return new_map

    def select_Move(self, pos, new_pos, turn):
        index0 = self.find_Cell(pos)
        index1 = self.find_Cell(new_pos)
        try:
            if self.__readableMap[index1[0]][index1[1]] == 'x' or self.__OjectLayer[(index1[1], index1[0])].get_killable():
                print('Từ ô',index0,'đến ô', index1)
                self.__OjectLayer[(index0[1], index0[0])].triggered_effects()
                self.__OjectLayer[(index1[1], index1[0])] = self.__OjectLayer[(index0[1], index0[0])]
                self.__OjectLayer[(index0[1], index0[0])] = None
                turn += 1
                print("Turn", turn)
        except:
            pass
        self.__readableMap = self.convert_to_readable()
        self.deseclect()
        return turn

    def is_checkmate(self):
        pass

    def is_finished(self):
        if self.count_on_rMap('king') == 1:
            return True
        else:
            return False

    def update(self, phase):
        Phase = phase
        updating = True
        if self.is_finished():
            Phase = 4
        elif phase == 0:
            print("Bắt đầu lượt mới")
            Phase = 1
        elif phase == 3:
            print("Kết thúc lượt")
            Phase = 0
        for i in range(8):
            for j in range(8):
                try:
                    self.__OjectLayer[(j, i)].update(self.__OjectLayer, self.__readableMap, (j, i), phase)
                except:
                    pass
            updating = False
        if not updating:
            return Phase