#FLM: Print all n and o kerning pairs

# Description:
# Print all n and o kerning pairs values

# Credits:
# Pablo Impallari

# Dependencies
from robofab.world import CurrentFont

# Clear Output windows
from FL import *
fl.output=""

f = CurrentFont()
kerning = f.kerning

# Print nLeft
nLeft = kerning.getLeft('n')
for pair in nLeft:
  print str(pair[0][0]) + ', ' + str(pair[0][1]) + ', ' + str(pair[1])
  
print ""

# Print nRight 
nRight = kerning.getRight('n')
for pair in nRight:
  print str(pair[0][0]) + ', ' + str(pair[0][1]) + ', ' + str(pair[1])

print ""

# Print oLeft
nLeft = kerning.getLeft('o')
for pair in nLeft:
  print str(pair[0][0]) + ', ' + str(pair[0][1]) + ', ' + str(pair[1])

print ""

# Print oRight 
nRight = kerning.getRight('o')
for pair in nRight:
  print str(pair[0][0]) + ', ' + str(pair[0][1]) + ', ' + str(pair[1])

print "Done!"