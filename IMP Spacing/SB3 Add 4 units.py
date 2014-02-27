#FLM: Add 2 Units to each side to current glyph

# Description:
# Increase current glyph sidebearings by 2 units on each side

# Credits:
# Pablo Impallari
# http://www.impallari.com

from robofab.world import CurrentFont,CurrentGlyph

f = CurrentFont()
g = CurrentGlyph()

OldLeft = g.leftMargin
OldRight = g.rightMargin 

g.leftMargin = OldLeft + 2
g.rightMargin = OldRight + 2

f.update()

