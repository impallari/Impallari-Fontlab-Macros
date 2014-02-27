#FLM: Save EPS from selected Glyph

# Description:
# Generate a EPS file for the Selected Glyph

# Credits:
# Pablo Impallari
# http://www.impallari.com

import os.path
from FL import *
from robofab.world import CurrentFont

# Get current Glyphs
f = CurrentFont()
g = fl.glyph

# Get path and file name
path = f.path
dir, fileName = os.path.split(path)
filename = dir + '/' + g.name + '.eps'

# Generate EPS file
g.SaveEPS( filename )

