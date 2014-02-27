#FLM: 02 Clear All Anchors

# Description:
# Deletes all the anchors in the current font

# Credits:
# By Ben Kiel
# http://www.benkiel.com/typeDesign/

print "Starting..."

from robofab.world import CurrentFont
font = CurrentFont()

for glyph in font:
	glyph.clearAnchors()
	
font.update()

print "Done!"