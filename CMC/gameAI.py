# Tạm thời chưa có
import pygame.time
import pygame

import CMC.board as board
import CMC.chess as chess
import CMC.environment as env

BOT_Team = 'b'
Sim_Players = []
Sim_Board = 0
Sim_Turn = 0

def import_data(nBoard, nPlayer, nTurn):
    """
    Nạp dữ liệu cho AI
    :param nBoard: Bàn cờ (board.Board)
    :param nPlayer: Danh sách người chơi (player.Player)
    :return: None
    """
    global Sim_Board, Sim_Players, Sim_Turn, BOT_Team
    Sim_Players = []
    Sim_Turn = nTurn
    Sim_Board = nBoard.duplication()
    for player in nPlayer:
        if player.get_name() == 'BOT':
            BOT_Team = player.get_team()
        Sim_Players.append(player.duplication())

def pre_bot_turn(nBoard, nPlayer, nTurn):
    import_data(nBoard, nPlayer, nTurn)
    oBoard = Sim_Board.getoBoard()

    maxPoint = -999
    index0 = 0
    index1 = 0

    for object in oBoard.items():
        try:
            if object[1].get_team() == BOT_Team:
                print(object[1].convert_to_readable())
                selected, moves = Sim_Board.select_Chess((object[0][1], object[0][0]), 2, BOT_Team)
                index0 = (object[0][1], object[0][0])
                tPoint = -888
                tIndex = 0
                for move in moves:
                    sSim_Board = Sim_Board.duplication()
                    sSim_Board.select_Move(index0, move)
                    point = sSim_Board.get_Score(BOT_Team)
                    if point > tPoint:
                        tIndex = move
                if tPoint > maxPoint:
                    index1 = tIndex
                Sim_Board.deselect()
        except:
            pass
    nBoard.select_Chess(index0, 2, BOT_Team)
    nBoard.select_Move(index0, index1)
    return nTurn + 1



