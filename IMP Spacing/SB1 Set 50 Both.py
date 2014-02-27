#FLM: Set 50 50 sidebearings

# Description:
# Set base sidebearings

# Credits:
# Pablo Impallari
# http://www.impallari.com

from robofab.world import CurrentFont,CurrentGlyph

f = CurrentFont()
g = CurrentGlyph()

g.leftMargin = 50
g.rightMargin = 50

f.update()

