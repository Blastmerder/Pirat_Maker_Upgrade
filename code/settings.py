import json

# general setup
TILE_SIZE = 64
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
# WINDOW_WIDTH = 1920
# WINDOW_HEIGHT = 1080

ANIMATION_SPEED = 8

# editor graphics

EDITOR_DATA = {int(k): v for k, v in json.loads(open('editorData.json', 'r').read()).items()}


NEIGHBOR_DIRECTIONS = {
    'A': (0, -1),
    'B': (1, -1),
    'C': (1, 0),
    'D': (1, 1),
    'E': (0, 1),
    'F': (-1, 1),
    'G': (-1, 0),
    'H': (-1, -1)
}

LEVEL_LAYERS = {
    'clouds': 1,
    'ocean': 2,
    'bg': 3,
    'water': 4,
    'main': 5
}

# colors 
SKY_COLOR = '#ddc6a1'
SEA_COLOR = '#92a9ce'
HORIZON_COLOR = '#f5f1de'
HORIZON_TOP_COLOR = '#d1aa9d'
LINE_COLOR = 'black'
BUTTON_BG_COLOR = '#33323d'
BUTTON_LINE_COLOR = '#f5f1de'
