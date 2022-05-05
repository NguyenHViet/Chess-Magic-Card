import pygame
import environment as env
import effect as ef
from card import Card
import chess
import random

listImage = {
    'b': {
        'b':pygame.image.load('img\\b_bishop.png'), 'k':pygame.image.load('img\\b_king.png'),
        'kn':pygame.image.load('img\\b_knight.png'), 'p':pygame.image.load('img\\b_pawn.png'),
        'q':pygame.image.load('img\\b_queen.png'), 'r':pygame.image.load('img\\b_rook.png')
    },
    'w': {
        'b':pygame.image.load('img\\w_bishop.png'), 'k':pygame.image.load('img\\w_king.png'),
        'kn':pygame.image.load('img\\w_knight.png'), 'p':pygame.image.load('img\\w_pawn.png'),
        'q':pygame.image.load('img\\w_queen.png'), 'r':pygame.image.load('img\\w_rook.png')
    },
    'GEI': {
        'Normal':pygame.image.load('img\\GEI\\classic_normal.png'),
        'Darken':pygame.image.load('img\\GEI\\darkcell.png'),
        'Move':pygame.image.load('img\\GEI\\move.png'),
        'Choice':pygame.image.load('img\\GEI\\choice.png'),
        'Hover':pygame.image.load('img\\GEI\\choice_magic.png'),
        'Card_Hover':pygame.image.load('img\\GEI\\card_hover.png'),
        'Card_Picking':pygame.image.load('img\\GEI\\picking_card.png'),
        'Card_Cell':pygame.image.load('img\\GEI\\card_area.png'),
    },
    'GUI': {
        'EndTurn': pygame.image.load('img\\GUI\\end_turn_button.png'),
        'Choice':pygame.image.load('img\\GUI\\choice_white.png'),
        'Pause':pygame.image.load('img\\GUI\\pause_button.png'),
        'Button':pygame.image.load('img\\GUI\\button.png'),
        'Hover_Button':pygame.image.load('img\\GUI\\button_hover.png'),
        'Black Timer':pygame.image.load('img\\GUI\\b_timer.png'),
        'White Timer':pygame.image.load('img\\GUI\\w_timer.png'),
        'Actions': pygame.image.load('img\\GUI\\actions.png')
    },
    'Cards': {
        '01':pygame.image.load('img\\Card\\01.png'),
        '02':pygame.image.load('img\\Card\\02.png'),
        '03':pygame.image.load('img\\Card\\03.png'),
        '04':pygame.image.load('img\\Card\\04.png'),
        '05':pygame.image.load('img\\Card\\05.png'),
        '06':pygame.image.load('img\\Card\\06.png')
    },
    'Desert': {
        'Normal':pygame.image.load('img\\Environment\\desert_normal.png'),
        'Speacial':pygame.image.load('img\\Environment\\derest_speacial.png')
    },
    'Frozen_river':{
        'Normal':pygame.image.load('img\\Environment\\frozen_river_normal.png'),
        'Speacial':pygame.image.load('img\\Environment\\frozen_river_speacial.png'),
        'Triggered_effect':pygame.image.load('img\\Environment\\frozen_river_hole.png')
    },
    'Foggy_forest': {
        'Normal':pygame.image.load('img\\Environment\\foggy_forest_normal.png'),
        'Speacial':pygame.image.load('img\\Environment\\foggy_forest_speacial.png')
    },
    'Swamp': {
        'Normal':pygame.image.load('img\\Environment\\swamp_normal.png'),
        'Speacial':pygame.image.load('img\\Environment\\swamp_speacial.png')
    },
    'Grassland': {
        'Normal':pygame.image.load('img\\Environment\\grassland.png')
    }
}

pygame.font.init()
font20 = pygame.font.Font('font\\Comfortaa-VariableFont_wght.ttf', 20)
font40 = pygame.font.Font('font\\static\\Comfortaa-SemiBold.ttf', 40)
font60 = pygame.font.Font('font\\static\\Comfortaa-SemiBold.ttf', 60)

EFFECT = {

}

DECK = [
    Card('Tiến Công', 2, listImage['Cards']['01'], 'Tiến thẳng hoặc chéo về phía trước 1 ô', 'ActiveEffects', 2, [ef.Effect('PushChess', turns = 1, phase = 3, value = 1)], directions = ['Ahead Left', 'Ahead', 'Ahead Right'], killable = False),
    Card('Rút Lui', 2, listImage['Cards']['02'], 'Lùi hoặc chéo về phía sau 1 ô', 'ActiveEffects', 2, [ef.Effect('PushChess', turns = 1, phase = 3, value = 1)], directions = ['Back Left', 'Back', 'Back Right'], killable = False),
    Card('Tấn Công Mạn Sườn', 2, listImage['Cards']['03'], 'Đi ngang sang trái hoặc phải 1 ô', 'ActiveEffects', 2, [ef.Effect('PushChess', turns = 1, phase = 3, value = 1)], directions = ['Left', 'Right'], killable = False),
    Card('Đánh Phủ Đầu', 3, listImage['Cards']['04'], 'Tấn công về phía trước 2 ô', 'ActiveEffects', 2, [ef.Effect('PushChess', turns = 1, phase = 3, value = 2)], directions = ['Ahead'], killable = True),
    Card('Đánh Phủ Đầu', 3, listImage['Cards']['05'], 'Tấn công về phía trước 2 ô', 'ActiveEffects', 2, [ef.Effect('PushChess', turns = 1, phase = 3, value = 1)], directions=['Back'], killable = True),
    Card('Linh Động Chiến Trường', 3, listImage['Cards']['06'], 'Di chuyển về 1 hướng bất kỳ 2 ô', 'ActiveEffects', 2, [ef.Effect('PushChess', turns=1, phase=3, value=1)], directions=['Ahead Left', 'Ahead', 'Ahead Right', 'Back Left', 'Back', 'Back Right', 'Left', 'Right'], killable=False)
]

ENVIRONMENT = {
    'Desert':env.Desert(listImage['Desert']),
    'Frozen_river':env.Frozen_river(listImage['Frozen_river']),
    'Foggy_forest':env.Foggy_forest(listImage['Foggy_forest']),
    'Swamp':env.Swamp(listImage['Swamp']),
    'Grassland':env.Grassland(listImage['Grassland'])
}

print(ENVIRONMENT['Grassland'])
def create_area(type_of_environment):
    """
    Hàm tạo hình dạng map
    :param type_of_environment: Tên môi trường (str)
    :return: Hình dạng map (list of image)
    """

    image = 'img\\Environment\\'
    area = list()
    cell_posision = list()
    count = int(0)

    while(count < 12):
        x = random.randint(0, 7)
        y = random.randint(1, 7)
        if (x, y) in cell_posision:
            pass
        else:
            cell_posision.append((x, y))
            count += 1

    count = 0
    for i in range(8):
        area.append([])
        for j in range(8):
            if ((i, j) in cell_posision) and (count < 12):
                if type_of_environment == 'Frozen_river':
                    area[i].append(listImage['Frozen_river']['Speacial'])
                elif type_of_environment == 'Swamp':
                    area[i].append(listImage['Swamp']['Speacial'])
                count += 1
            else:
                if type_of_environment == 'Frozen_river':
                    area[i].append((listImage['Frozen_river']['Normal']))
                elif type_of_environment == 'Swamp':
                    area[i].append(listImage['Swamp']['Normal'])
    return area

frozen_river_map = create_area('Frozen_river')
swamp_map = create_area('Swamp')