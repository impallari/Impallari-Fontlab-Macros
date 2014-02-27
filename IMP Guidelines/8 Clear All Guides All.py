#FLM: Clear All Guidelines on All Glyphs

# Description:
# Clear All Guidelines of the current font
# Both Global and Local

# Credits:
# Pablo Impallari
# http://www.impallari.com

from FL import *

# Get current Glyphs
f = fl.font

# Clear Global Guidelines
fvguides = f.vguides
fvguides.clean()

fhguides = f.hguides
fhguides.clean()

# Clear Local guidelines
for g in f.glyphs:

	gvguides = g.vguides
	gvguides.clean()
	
	ghguides = g.hguides
	ghguides.clean()
	
# Update font
fl.UpdateGlyph()


