#FLM: Test all Kerning Pairs in words

# Description:
# Export a list of all kerning pairs surrounded by nononon For further inspection

# Dependencies
from robofab.world import CurrentFont
import os.path

# Clear Output windows
from FL import *
fl.output=""

# Get Kerning Values
f = CurrentFont()
kerning = f.kerning

#Get Path to write the results
path = f.path
dir, fileName = os.path.split(path)
output = open(dir+'/AllKernInWords.txt', 'w')

# Print all Pairs
for (left, right), value in kerning.items():
    output.write( '/n/n/o/n/' + str(left)+'/'+str(right)+'/n/o/n/n')
    output.write( '\n')

output.close()	
print "Done!"