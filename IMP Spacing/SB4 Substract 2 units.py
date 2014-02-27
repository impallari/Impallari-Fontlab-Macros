#FLM: Substract 1 Units to each side to current glyph

# Description:
# Substract current glyph sidebearings by 1 units on each side

# Credits:
# Pablo Impallari
# http://www.impallari.com

from robofab.world import CurrentFont,CurrentGlyph

f = CurrentFont()
g = CurrentGlyph()

OldLeft = g.leftMargin
OldRight = g.rightMargin 

g.leftMargin = OldLeft - 1
g.rightMargin = OldRight - 1

f.update()