#FLM: Print selected Glyph kerns

# Description:
# Print all Kerning Pairs for the selected glyph

# Credits:
# Pablo Impallari

# Clear Output windows
from FL import *
fl.output=""

# Display Kerning Pairs
from robofab.world import *
f = CurrentFont()
g = CurrentGlyph()
kerning = f.kerning

print "----------"
print "Kerning Pairs for /" + str(g.name)
print ""
print "1st in Pair:"
print "------------"

currentLeft = kerning.getLeft(g.name)
for pair in currentLeft:
  print str(pair[0][0]) + ', ' + str(pair[0][1]) + ', ' + str(pair[1]) 

print ""

print "2nd in Pair:"
print "------------"

currentRight = kerning.getRight(g.name)
for pair in currentRight:
  print str(pair[0][0]) + ', ' + str(pair[0][1]) + ', ' + str(pair[1])

print ""

print "----------"