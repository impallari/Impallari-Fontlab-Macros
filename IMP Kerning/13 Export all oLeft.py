#FLM: Export all oLeft pairs to CSV

# To-do:
# It only report main pairs, not fully expanded if the font uses classes

# Credits:
# Pablo Impallari

import os.path
from robofab.world import CurrentFont

f = CurrentFont()
kerning = f.kerning

#Do some work
print "Working..."
path = f.path
dir, fileName = os.path.split(path)

output = open(dir+'/my-oLeft-Kerns.csv', 'w')

# Print oLeft
nLeft = kerning.getLeft('o')
for pair in nLeft:
  output.write( str(pair[0][0])+', '+str(pair[0][1])+', '+str(pair[1]))
  output.write( '\n')

output.close()
print "Done!"