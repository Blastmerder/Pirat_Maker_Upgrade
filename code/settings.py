# general setup
TILE_SIZE = 64
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
# WINDOW_WIDTH = 1920
# WINDOW_HEIGHT = 1080

ANIMATION_SPEED = 8

# editor graphics 
EDITOR_DATA = {
	0: {'style': 'player', 'type': 'object', 'menu': None, 'menu_surf': None, 'preview': None, 'graphics': '../graphics/player/idle_right', 'settings': None},
	1: {'style': 'sky',    'type': 'object', 'menu': None, 'menu_surf': None, 'preview': None, 'graphics': None, 'settings': None},
	
	2: {'style': 'terrain', 'type': 'tile', 'menu': 'terrain', 'menu_surf': '../graphics/menu/land.png',  'preview': '../graphics/preview/land.png',  'graphics': None, 'settings': None},
	3: {'style': 'water',   'type': 'tile', 'menu': 'terrain', 'menu_surf': '../graphics/menu/water.png', 'preview': '../graphics/preview/water.png', 'graphics': '../graphics/terrain/water/animation', 'settings': None},
	
	4: {'style': 'coin', 'type': 'tile', 'menu': 'coin', 'menu_surf': '../graphics/menu/gold.png',    'preview': '../graphics/preview/gold.png',    'graphics': '../graphics/items/gold', 'settings': None},
	5: {'style': 'coin', 'type': 'tile', 'menu': 'coin', 'menu_surf': '../graphics/menu/silver.png',  'preview': '../graphics/preview/silver.png',  'graphics': '../graphics/items/silver', 'settings': None},
	6: {'style': 'coin', 'type': 'tile', 'menu': 'coin', 'menu_surf': '../graphics/menu/diamond.png', 'preview': '../graphics/preview/diamond.png', 'graphics': '../graphics/items/diamond', 'settings': None},

	7:  {'style': 'enemy', 'type': 'tile', 'menu': 'enemy', 'menu_surf': '../graphics/menu/spikes.png',      'preview': '../graphics/preview/spikes.png',      'graphics': '../graphics/enemies/spikes', 'settings': None},
	8:  {'style': 'enemy', 'type': 'tile', 'menu': 'enemy', 'menu_surf': '../graphics/menu/tooth.png',       'preview': '../graphics/preview/tooth.png',       'graphics': '../graphics/enemies/tooth/idle', 'settings': None},
	9:  {'style': 'enemy', 'type': 'tile', 'menu': 'enemy', 'menu_surf': '../graphics/menu/shell_left.png',  'preview': '../graphics/preview/shell_left.png',  'graphics': '../graphics/enemies/shell_left/idle', 'settings': None},
	10: {'style': 'enemy', 'type': 'tile', 'menu': 'enemy', 'menu_surf': '../graphics/menu/shell_right.png', 'preview': '../graphics/preview/shell_right.png', 'graphics': '../graphics/enemies/shell_right/idle', 'settings': None},
	
	11: {'style': 'palm_fg', 'type': 'object', 'menu': 'palm fg', 'menu_surf': '../graphics/menu/small_fg.png', 'preview': '../graphics/preview/small_fg.png', 'graphics': '../graphics/terrain/palm/small_fg', 'settings': None},
	12: {'style': 'palm_fg', 'type': 'object', 'menu': 'palm fg', 'menu_surf': '../graphics/menu/large_fg.png', 'preview': '../graphics/preview/large_fg.png', 'graphics': '../graphics/terrain/palm/large_fg', 'settings': None},
	13: {'style': 'palm_fg', 'type': 'object', 'menu': 'palm fg', 'menu_surf': '../graphics/menu/left_fg.png',  'preview': '../graphics/preview/left_fg.png',  'graphics': '../graphics/terrain/palm/left_fg', 'settings': None},
	14: {'style': 'palm_fg', 'type': 'object', 'menu': 'palm fg', 'menu_surf': '../graphics/menu/right_fg.png', 'preview': '../graphics/preview/right_fg.png', 'graphics': '../graphics/terrain/palm/right_fg', 'settings': None},

	15: {'style': 'palm_bg', 'type': 'object', 'menu': 'palm bg', 'menu_surf': '../graphics/menu/small_bg.png', 'preview': '../graphics/preview/small_bg.png', 'graphics': '../graphics/terrain/palm/small_bg', 'settings': None},
	16: {'style': 'palm_bg', 'type': 'object', 'menu': 'palm bg', 'menu_surf': '../graphics/menu/large_bg.png', 'preview': '../graphics/preview/large_bg.png', 'graphics': '../graphics/terrain/palm/large_bg', 'settings': None},
	17: {'style': 'palm_bg', 'type': 'object', 'menu': 'palm bg', 'menu_surf': '../graphics/menu/left_bg.png',  'preview': '../graphics/preview/left_bg.png',  'graphics': '../graphics/terrain/palm/left_bg', 'settings': None},
	18: {'style': 'palm_bg', 'type': 'object', 'menu': 'palm bg', 'menu_surf': '../graphics/menu/right_bg.png', 'preview': '../graphics/preview/right_bg.png', 'graphics': '../graphics/terrain/palm/right_bg', 'settings': None},
	19: {'style': 'checkpoint', 'type': 'object', 'menu': 'checkpoint', 'menu_surf': '../graphics/menu/checkpoint.png', 'preview': '../graphics/preview/checkpoint.png', 'graphics': '../graphics/checkpoint', 'settings': None},

	20: {'style': 'setting_button_deselect', 'type': None, 'menu': None, 'menu_surf': '../graphics/settings_gui/settings.png', 'preview': None, 'graphics': None, 'settings': 'open_settings'},

}

NEIGHBOR_DIRECTIONS = {
	'A': (0,-1),
	'B': (1,-1),
	'C': (1,0),
	'D': (1,1),
	'E': (0,1),
	'F': (-1,1),
	'G': (-1,0),
	'H': (-1,-1)
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
