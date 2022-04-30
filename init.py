import pygame

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
    'classic': {
        'Normal':pygame.image.load('img\\classic_normal.png'),
        'Darken':pygame.image.load('img\\darkcell.png'),
        'Move':pygame.image.load('img\\move.png'),
        'Choice':pygame.image.load('img\\choice.png')
    }
}

"""
'desert': {
        'Normal':pygame.image.load('img\desert_normal.png'),
        'Speacial':pygame.image.load('img\desert_speacial.png')
    },
    'frozen_river': {
        'Normal':pygame.image.load('img\\frozen_river_normal.png'),
        'Speacial':pygame.image.load('img\\frozen_river_speacial.png')
    },
    'swamp': {
        'Normal':pygame.image.load('img\swamp_normal.png'),
        'Speacial':pygame.image.load('img\swamp_speacial.png')
    },
    'foggy_forest': {
        'Normal':pygame.image.load('img\\foggy_forest_normal.png'),
        'Speacial':pygame.image.load('img\\foggy_forest_speacial.png')
    },
    'valley': {
        'Normal':pygame.image.load('img\\valley_normal.png'),
        'Speacial':pygame.image.load('img\\valley_speacial.png')
    },
    'wind_plateau': {
        'Normal':pygame.image.load('img\wind_plateau_normal.png'),
        'Speacial':pygame.image.load('img\wind_plateau_speacial.png')
    }
"""