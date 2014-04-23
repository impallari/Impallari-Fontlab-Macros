#FLM: Center of Italic on All Glyphs

# Description:
# Place a guideline in the center of the selected glyph
# Italic Version - All Glyphs

# Credits:
# Pablo Impallari
# http://www.impallari.com

from FL import *

# Get current Glyphs
f = fl.font

# Find Angle
angle = f.italic_angle

if angle <= -1 :
	angle = angle * -1

for g in f.glyphs:

	# Clear Local Guidelines
	gvguides = g.vguides
	gvguides.clean()

	# Find the center of the glyph
	centro = g.width / 2

	# Place Guideline
	g.vguides.append(Guide(0, angle))
	g.vguides.append(Guide(centro, angle))
	g.vguides.append(Guide(g.width, angle))
	
# Update font
fl.UpdateGlyph()


