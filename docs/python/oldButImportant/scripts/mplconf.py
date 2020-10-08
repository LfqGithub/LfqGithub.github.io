
from matplotlib.pyplot import *
from pylab import *

colors = {
		'red' : '#dc322f',
		'red_bold' : '#cb4b16',
		'green' : '#859900',
		'green_bold' : '#586e75',
		'yellow' : '#b58900',
		'yellow_bold' : '#657b83',
		'blue' : '#268bd2',
		'blue_bold' : '#839496',
		'magenta' : '#d33682',
		'magenta_bold' : '#6c71c4',
		'cyan' : '#2aa198',
		'cyan_bold' : '#93a1a1',
		'black' : '#073642',
		'white' : '#eee8d5',
		'white_bold' : '#fdf6e3',
		}

_lines = {
		'linewidth' : 1.8,
		'marker' : 'o',
		}
rc('lines',**_lines)

_font = {
		'family' : 'serif',
		'serif': 'Arial',
		}
#rc('font',**_font)

_axes = {
		'hold' : True,
		'facecolor' : 'white',
		'linewidth' : 2.,
		'grid' : True,
		'labelsize' : 24,
		'color_cycle' : [colors['blue'], colors['green'], 
			colors['red'], colors['cyan'], colors['magenta'],
			colors['yellow'],colors['black'], 
			colors['blue_bold'],colors['green_bold'],colors['red_bold'],
			colors['cyan_bold'],colors['magenta_bold'],colors['yellow_bold'],
			],
		'titlesize' : 30,
				
		}
rc('axes',**_axes)

_legend = {
		'isaxes' : True,
		'numpoints' : 3,
		'markerscale' : 0.6,
		'frameon' : False,
		'fontsize' : 24,
		}
rc('legend',**_legend)

_xtick = {
		'labelsize' : 24,
		}
rc('xtick',**_xtick)

_ytick = {
		'labelsize' : 24,
		}
rc('ytick',**_ytick)

_grid = {
		'linewidth' : 0.8,
		'color' : colors['black'],
		'linestyle' : '--'
		}
rc('grid',**_grid)

_figure = {
		'facecolor' : '1.',
		}
rc('figure',**_figure)

_savefig = {
		'dpi' : 200,
		'facecolor' : 'white',
		'edgecolor' : 'white',
		}
rc('savefig',**_savefig)
