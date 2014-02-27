#FLM: Clear Local Guidelines on Current Glyph

# Description:
# Clear Local Guidelines on current glyph

# Credits:
# Pablo Impallari
# http://www.impallari.com

from FL import *

# Get current Glyphs
f = fl.font
g = fl.glyph

# Glear Local Guides
gvguides = g.vguides
gvguides.clean()
	
ghguides = g.hguides
ghguides.clean()
	
# Update font
fl.UpdateGlyph()


