import pygame
import copy
import CMC.chess as chess
import CMC.init as init
import CMC.cell as cell
import CMC.effect as ef

wPawn = [
    [10.0,  10.0,  10.0,  10.0,  10.0,  10.0,  10.0,  10.0],
    [ 5.0,   5.0,   5.0,   5.0,   5.0,   5.0,   5.0,   5.0],
    [ 1.0,   1.0,   2.0,   3.0,   3.0,   2.0,   1.0,   1.0],
    [ 0.5,   0.5,   1.0,   2.5,   2.5,   1.0,   0.5,   0.5],
    [ 0.0,   0.0,   0.0,   2.0,   2.0,   0.0,   0.0,   0.0],
    [ 0.5,  -0.5,  -1.0,   0.0,   0.0,  -1.0,  -0.5,   0.5],
    [ 0.5,   1.0,   1.0,  -2.0,  -2.0,   1.0,   1.0,   0.5],
    [ 0.0,   0.0,   0.0,   0.0,   0.0,   0.0,   0.0,   0.0]
]

bPawn = copy.copy(wPawn)
bPawn.reverse()

wKnight = bKnight = [
    [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0],
    [-4.0, -2.0,  0.0,  0.0,  0.0,  0.0, -2.0, -4.0],
    [-3.0,  0.5,  1.0,  1.5,  1.5,  1.0,  0.5, -3.0],
    [-3.0,  0.0,  1.5,  2.0,  2.0,  1.5,  0.0, -3.0],
    [-3.0,  0.0,  1.5,  2.0,  2.0,  1.5,  0.0, -3.0],
    [-3.0,  0.5,  1.0,  1.5,  1.5,  1.0,  0.5, -3.0],
    [-4.0, -2.0,  0.0,  0.5,  0.5,  0.0, -2.0, -4.0],
    [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0]
]

wBishop = [
    [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0],
    [-1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0],
    [-1.0,  0.0,  0.5,  1.0,  1.0,  0.5,  0.0, -1.0],
    [-1.0,  0.5,  0.5,  1.0,  1.0,  0.5,  0.5, -1.0],
    [-1.0,  0.0,  1.0,  1.0,  1.0,  1.0,  0.0, -1.0],
    [-1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0, -1.0],
    [-1.0,  0.5,  0.0,  0.0,  0.0,  0.0,  0.5, -1.0],
    [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0]
]

bBishop = copy.copy(wBishop)
bBishop.reverse()

wRook = [
    [ 0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
    [ 0.5,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  0.5],
    [-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [ 0.0,  0.0,  0.0,  0.5,  0.5,  0.0,  0.0,  0.0]
]

bRook = copy.copy(wRook)
bRook.reverse()

wQueen = bQueen = [
    [-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0],
    [-1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0],
    [-1.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],
    [-0.5,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],
    [ 0.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],
    [-1.0,  0.5,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],
    [-1.0,  0.0,  0.5,  0.0,  0.0,  0.0,  0.0, -1.0],
    [-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0]
]

wKing = [
    [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [-2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0],
    [-1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0],
    [ 2.0,  2.0,  0.0,  0.0,  0.0,  0.0,  2.0,  2.0],
    [ 2.0,  3.0,  1.0,  0.0,  0.0,  1.0,  3.0,  2.0]
]

bKing = copy.copy(wKing)
bKing.reverse()

class Board:
    """
    Lớp "Bàn cờ"
    """
    def __init__(self, x, y, width, pTeam, enviroment, lImg):
        """
        Hàm khởi tạo
        :param x: Tạo độ x của bàn cờ (int)
        :param y: Tạo độ y của bàn cờ (int)
        :param width: Chiều rộng của bàn cờ (int)
        :param pTeam: Chiều dài của bàn cờ (int)
        :param enviroment: Môi trường của bàn cờ (environment.Environment)
        :param lImg: Danh sách hình ảnh (list(pygame.image))
        """
        self.__x = x
        self.__y = y
        self.__width = width
        self.__enviroment = enviroment
        oTeam = 'b'
        if pTeam == 'b':
            oTeam == 'w'
        else:
            oTeam == 'b'
        # Tạo phần layer các thực thể trên bàn cờ
        self.__OjectLayer = {(0, 0): chess.Rook(oTeam, 'downward', lImg[oTeam]['Rook']), (1, 0): chess.Knight(oTeam, 'downward', lImg[oTeam]['Knight']),
                             (2, 0): chess.Bishop(oTeam, 'downward', lImg[oTeam]['Bishop']), (3, 0): chess.Queen(oTeam, 'downward', lImg[oTeam]['Queen']),
                             (4, 0): chess.King(oTeam, 'downward', lImg[oTeam]['King']), (5, 0): chess.Bishop(oTeam, 'downward', lImg[oTeam]['Bishop']),
                             (6, 0): chess.Knight(oTeam, 'downward', lImg[oTeam]['Knight']), (7, 0): chess.Rook(oTeam, 'downward', lImg[oTeam]['Rook']),
                             (0, 1): chess.Pawn(oTeam, 'downward', lImg[oTeam]['Pawn']), (1, 1): chess.Pawn(oTeam, 'downward', lImg[oTeam]['Pawn']),
                             (2, 1): chess.Pawn(oTeam, 'downward', lImg[oTeam]['Pawn']), (3, 1): chess.Pawn(oTeam, 'downward', lImg[oTeam]['Pawn']),
                             (4, 1): chess.Pawn(oTeam, 'downward', lImg[oTeam]['Pawn']), (5, 1): chess.Pawn(oTeam, 'downward', lImg[oTeam]['Pawn']),
                             (6, 1): chess.Pawn(oTeam, 'downward', lImg[oTeam]['Pawn']), (7, 1): chess.Pawn(oTeam, 'downward', lImg[oTeam]['Pawn']),

                             (0, 2): None, (1, 2): None, (2, 2): None, (3, 2): None,
                             (4, 2): None, (5, 2): None, (6, 2): None, (7, 2): None,
                             (0, 3): None, (1, 3): None, (2, 3): None, (3, 3): None,
                             (4, 3): None, (5, 3): None, (6, 3): None, (7, 3): None,
                             (0, 4): None, (1, 4): None, (2, 4): None, (3, 4): None,
                             (4, 4): None, (5, 4): None, (6, 4): None, (7, 4): None,
                             (0, 5): None, (1, 5): None, (2, 5): None, (3, 5): None,
                             (4, 5): None, (5, 5): None, (6, 5): None, (7, 5): None,

                             (0, 6): chess.Pawn(pTeam, 'upward', lImg[pTeam]['Pawn']), (1, 6): chess.Pawn(pTeam, 'upward', lImg[pTeam]['Pawn']),
                             (2, 6): chess.Pawn(pTeam, 'upward', lImg[pTeam]['Pawn']), (3, 6): chess.Pawn(pTeam, 'upward', lImg[pTeam]['Pawn']),
                             (4, 6): chess.Pawn(pTeam, 'upward', lImg[pTeam]['Pawn']), (5, 6): chess.Pawn(pTeam, 'upward', lImg[pTeam]['Pawn']),
                             (6, 6): chess.Pawn(pTeam, 'upward', lImg[pTeam]['Pawn']), (7, 6): chess.Pawn(pTeam, 'upward', lImg[pTeam]['Pawn']),
                             (0, 7): chess.Rook(pTeam, 'upward', lImg[pTeam]['Rook']), (1, 7): chess.Knight(pTeam, 'upward', lImg[pTeam]['Knight']),
                             (2, 7): chess.Bishop(pTeam, 'upward', lImg[pTeam]['Bishop']), (3, 7): chess.Queen(pTeam, 'upward', lImg[pTeam]['Queen']),
                             (4, 7): chess.King(pTeam, 'upward', lImg[pTeam]['King']), (5, 7): chess.Bishop(pTeam, 'upward', lImg[pTeam]['Bishop']),
                             (6, 7): chess.Knight(pTeam, 'upward', lImg[pTeam]['Knight']), (7, 7): chess.Rook(pTeam, 'upward', lImg[pTeam]['Rook'])}
        self.__GEI = lImg['GEI']
        # Tạo phần layer các ô trên bàn cờ
        interval = self.__width / 8
        self.__enviroment.create_map(self)
        self.__CellLayer = []
        self.clear_map()

        # Tạo phần readable để làm input cho các hàm khác
        self.__readableMap = [[' ' for i in range (8)] for i in range(8)]
        self.__readableMap = self.convert_to_readable()

    def duplication(self):
        """
        Tạo bản sao của bàn cờ
        :return: Bản sao của bàn cờ (board.Board)
        """
        dup_board = copy.copy(self)
        self.__OjectLayer = copy.copy(dup_board.getoBoard())
        oBoard = dup_board.getoBoard()
        for chess in oBoard.items():
            try:
                oBoard[chess[0]] = chess[1].duplication()
            except:
                pass
        env = self.__enviroment.duplication()
        dup_board.set_env(env)
        dup_board.set_cellLayer([])
        return copy.deepcopy(dup_board)


    def clear_map(self):
        """
        Thiết lập lại danh sách ô cờ và danh sách các đánh dấu của quân cờ
        :return: None
        """
        interval = self.__width / 8
        self.__CellLayer = []
        for x in range(8):
            self.__CellLayer.append([])
            for y in range(8):
                self.__CellLayer[x].append(
                    cell.Cell((x * interval) + self.__y, (y * interval) + self.__x, self.__GEI['Empty']))
        self.__readableMap = [[' ' for i in range(8)] for i in range(8)]
        self.__readableMap = self.convert_to_readable()

    def get_x(self):
        """
        Lấy tạo độ x của bàn cờ
        :return: Tạo độ x của bàn cờ (int)
        """
        return self.__x

    def get_y(self):
        """
        Lấy tạo độ y của bàn cờ
        :return: Tạo độ y của bàn cờ (int)
        """
        return self.__y

    def draw(self, win):
        """
        Hàm in các hình ảnh lên cửa sổ hiển thị
        :param win: Cửa sổ hiển thị (pygame.display)
        :return: None
        """
        self.__enviroment.draw(win)
        interval = self.__width / 8
        for row in range(8):
            for col in range(8):
                if (row+col) % 2 == 0:
                    win.blit(self.__GEI['Darker'] ,(self.__CellLayer[row][col].get_x(), self.__CellLayer[row][col].get_y()))
                # if self.__CellLayer[row][col].is_mouse_hovering(pygame.mouse.get_pos()):
                #     win.blit(self.__GEI['Hover'], (self.__CellLayer[row][col].get_x(), self.__CellLayer[row][col].get_y()))
                if 'x' in self.__readableMap[col][row]:
                    win.blit(self.__GEI['Move'] ,(self.__CellLayer[row][col].get_x(), self.__CellLayer[row][col].get_y()))
                elif ':' in (self.__readableMap[col][row]):
                    win.blit(self.__GEI['Choice'],
                             (self.__CellLayer[row][col].get_x(), self.__CellLayer[row][col].get_y()))
                # elif '#' in (self.__readableMap[col][row]):
                #     win.blit(self.__GEI['Hover'],
                #              (self.__CellLayer[row][col].get_x(), self.__CellLayer[row][col].get_y()))
                if not self.__OjectLayer[(row, col)] == None:
                    self.__OjectLayer[(row, col)].draw(win, self.__CellLayer[row][col].get_pos(), interval)
                self.__CellLayer[row][col].draw(win)

    def printMap(self):
        """
        In bàn cờ dưới dạng đọc được
        :return: None
        """
        for i in range(8):
            print(" ".join(["{:^8}" for j in range(8)]).format(*self.__readableMap[i]))

    def count_on_rMap(self, object):
        """
        Đếm trên bàn cờ dựa theo dữ liệu object đầu vào
        :param object: Dữ liệu cần tìm trên bàn cờ (str)
        :return: Số lượng tìm thấy (int)
        """
        count = 0
        for items in self.__readableMap:
            for item in items:
                if object in item:
                    count += 1
        return count

    def find_Cell(self, pos):
        """
        Lấy tọa đồ trên bàn cờ dựa theo vị trí con trỏ chuột nhấp vào
        :param pos: Vị trí con trỏ chuột (tuple(int, int))
        :return: tọa độ trên bàn cờ (tuple(int, int))
        """
        interval = self.__width / 8
        y, x = pos
        row = (x - self.__x) // interval
        col = (y - self.__y) // interval
        return int(row), int(col)

    def check_Team(self, index, teamCheck):
        """
        Kiểm tra đội dựa theo đầu vào
        :param index: Tọa độ trên bàn cờ (tuple(int, int))
        :param teamCheck: Giá trị đội cần kiểm tra (str)
        :return: Kết quả (bool)
        """
        try:
            if self.__OjectLayer[index].get_team() == teamCheck:
                return True
            else:
                return False
        except:
            return False

    def select_Chess(self, index, phase, playingTeam = 'b', set_move = True):
        """
        Chọn quân cờ
        :param index: Tọa độ trên bàn cờ (tuple(int, int)
        :param phase: Giai đoạn của lượt hiện tại (int)
        :param playingTeam: Đội đang chơi (str)
        :param set_move: Đánh dấu các ô có thể di chuyển của quân cờ (bool)
        :return: Kết quả (bool)
        """
        y, x = index
        moves = []
        if self.check_Team((x, y), playingTeam):
            # print("Team turn:", playingTeam)
            result = self.__OjectLayer[(x, y)].active_effects(self, index, phase)
            if ef.STATUS[1] in result:
                # print("Không thể chọn")
                return False
            self.__readableMap[index[0]][index[1]] += ':'
            if set_move:
                moves = self.__OjectLayer[(x, y)].get_moves(self, index, phase)
            # print("Chọn thành công quân cờ:", self.__readableMap[y][x])
            return True, moves
        else:
            # print("Không thể chọn")
            return False, moves

    def deselect(self):
        """
        Hủy chọn quân cờ
        :return: None
        """
        for i in range(8):
            for j in range(8):
                try:
                    self.__readableMap[i][j] = self.__OjectLayer[(j, i)].convert_to_readable()
                    self.__OjectLayer[(j, i)].set_killable(self, (i, j), 1, False)
                except:
                    if ' ' != self.__readableMap[i][j]:
                        self.__readableMap[i][j] = ' '

    def convert_to_readable(self):
        """
        Chuyển bàn cờ về dạng đọc được
        :return: Dạng đọc được của bàn cờ (list(list)))
        """
        new_map = self.__readableMap
        for i in range(8):
            for j in range(8):
                try:
                    new_map[i][j] = self.__OjectLayer[(j, i)].convert_to_readable()
                except:
                    new_map[i][j] = ' '
        return new_map

    def select_Move(self, index0, index1, triggeredEffect = True, swap = False, histLog = True):
        """
        Di chuyển quân cờ
        :param index0: Vị trí ban đầu
        :param index1: Vị trí mới
        :param triggeredEffect: Giảm cộng dồn hiệu ứng (bool)
        :param swap: Hoán đổi vị trí (bool)
        :param histLog: Thêm vào lịch sử (bool)
        :return: Kết quả (bool)
        """
        moved = False
        # Nhập thành
        if 'King:' in self.__readableMap[index0[0]][index0[1]] and 'Rookx' in self.__readableMap[index1[0]][index1[1]] and self.__OjectLayer[(index0[1], index0[0])].get_team() == self.__OjectLayer[(index1[1], index1[0])].get_team():
            if index0[1] > index1[1]:
                direction = -1
            else:
                direction = 1
            self.__OjectLayer[(index0[1] + direction*2, index0[0])] = self.__OjectLayer[(index0[1], index0[0])]
            self.__OjectLayer[(index0[1] + direction, index0[0])] = self.__OjectLayer[(index1[1], index1[0])]
            self.__OjectLayer[(index0[1], index0[0])] = None
            self.__OjectLayer[(index1[1], index1[0])] = None
            return True

        # Di chuyển quân cờ
        if index0 == index1:
            return  moved
        try:
            if 'x' in self.__readableMap[index1[0]][index1[1]]:
                try:
                    if self.__OjectLayer[(index1[1], index1[0])].get_killable():
                        sfx = pygame.mixer.Sound('assets/music/swords_hit.wav')
                        if '-' in self.__readableMap[index1[0]][index1[1]]:
                            sfx.set_volume(init.SETTINGS['Sound Volumn'] / 100)
                            sfx.play()
                    elif '-' in self.__readableMap[index1[0]][index1[1]]:
                        self.__enviroment.play_sfx()
                except:
                    pass
                if histLog:
                    init.HistoryLog.pop(0)
                    init.HistoryLog.append('{}: {} -> {}'.format(self.__OjectLayer[(index0[1], index0[0])].get_type(), index0, index1))
                # print('Từ ô',index0,'đến ô', index1)
                moved = True
                if triggeredEffect:
                    try:
                        self.__OjectLayer[(index1[1], index1[0])].triggered_effects()
                    except:
                        pass
                    self.__OjectLayer[(index0[1], index0[0])].triggered_effects()
                if swap:
                    swapObject = self.__OjectLayer[(index1[1], index1[0])]
                else:
                    swapObject = None
                self.__OjectLayer[(index1[1], index1[0])] = self.__OjectLayer[(index0[1], index0[0])]
                self.__OjectLayer[(index0[1], index0[0])] = swapObject
        except:
            pass
        if moved:
            self.__readableMap = self.convert_to_readable()
            self.deselect()
        return moved

    def controlledCells(self, phase, playingTeam = 'w'):
        """
        Đánh dấu các vị trí của quân đối thủ có thể chiếu vào
        :param phase: Giai đoạn của lượt hiện tại (int)
        :param playingTeam: Đội đang chơi (str)
        :return: None
        """
        for object in self.__OjectLayer.items():
            y, x = object[0]
            try:
                if object[1].get_team() != playingTeam:
                    object[1].active_effects(self, (x, y), 2)
                    object[1].get_moves(self, (x, y), phase, mark='#', killable=True)
                    object[1].unactive_effects()
            except:
                pass

    def is_checkmate(self):
        """
        Kiểm tra chiếu tướng
        :return: Kết quả (bool)
        """
        if self.count_on_rMap('King#') >= 1:
            return True
        else:
            return False

    def is_finished(self):
        """
        Kiểm tra kết thúc trận đấu
        :return: Kết quả (bool)
        """
        if self.count_on_rMap('King') <= 1:
            return True
        else:
            return False

    def update(self, phase, turn, playingTeam):
        """
        Cập nhập bàn cờ
        :param phase: Gia đoạn của lượt hiện tại (int)
        :param turn: Lượt hiện tại (int)
        :param playingTeam: Đội đang chơi (str)
        :return: Giai đoạn và lượt hiện tại (tuple(int, str))
        """
        Phase = phase
        self.__enviroment.apply_env_effect(self, turn, phase)
        for i in range(8):
            for j in range(8):
                try:
                    self.__OjectLayer[(j, i)].update(self, (i, j), phase)
                except:
                    pass
        if self.is_finished():
            Phase = chess.PHASE['Finish']
        elif phase == chess.PHASE['Start']:
            Phase = chess.PHASE['Picking']
            self.deselect()
            self.controlledCells(phase, playingTeam)
        elif phase == chess.PHASE['End']:
            turn += 1
            Phase = chess.PHASE['Start']
        return Phase, turn

    def getoBoard(self):
        """
        Lấy danh sách các đối tượng trên bàn cờ
        :return: Danh sách các đối tượng trên bàn cờ (dict(chess.Chess))
        """
        return self.__OjectLayer

    def getrBoard(self):
        """
        Lấy danh sách các ký hiệu trên bàn cờ
        :return: Danh sách các ký hiệu trên bàn cờ (list(list))
        """
        return self.__readableMap

    def getcBoard(self):
        """
        Lấy danh sách các ô trên bàn cờ
        :return: Danh sách các ô trên bàn cờ (list(list)))
        """
        return self.__CellLayer

    def get_Score(self, team):
        """
        Lấy tổng điểm theo đội
        :return:
        """
        sum = 0
        for object in self.__OjectLayer.items():
            try:
                if object[1].get_team() == team:
                    sum += (object[1].get_score() + globals()[object[1].convert_to_readable()][object[0][1]][object[0][0]])
                else:
                    sum -= (object[1].get_score() + globals()[object[1].convert_to_readable()][object[0][1]][object[0][0]])
            except:
                pass
        return sum

    def set_env(self, new_env):
        """
        Gán môi trường mới
        :param new_env: Môi trường mới (environment)
        :return: None
        """
        self.__enviroment = new_env

    def set_cellLayer(self, cellLayer):
        """
        Gán lớp ô cờ mới
        :param cellLayer: Lớp ô cờ mới (list(list(cell.Cell)))
        :return:
        """
        self.__GEI = []
        self.__CellLayer = cellLayer