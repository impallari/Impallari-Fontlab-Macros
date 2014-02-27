#FLM: Export nLeft to Lowercase pairs to CSV

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

output = open(dir+'/my-nLeft-toLower-Kerns.csv', 'w')

# Print nLeft
nLeft = kerning.getLeft('n')
rightList = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z');

for pair in nLeft:
  if pair[0][1] in rightList:
  	output.write( str(pair[0][0])+', '+str(pair[0][1])+', '+str(pair[1]))
  	output.write( '\n')

output.close()
print "Done!"