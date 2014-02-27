#FLM: Center of Current Glyph

# Description:
# Place a guideline in the center of the selected glyph

# Credits:
# Pablo Impallari
# http://www.impallari.com

from FL import *

# Get current Glyphs
f = fl.font
g = fl.glyph

# Clear old local v guides
gvguides = g.vguides
gvguides.clean()

# Find the center of the glyph and place new local guide
centro = g.width / 2
g.vguides.append(Guide(centro))
	
# Update font
fl.UpdateGlyph()


