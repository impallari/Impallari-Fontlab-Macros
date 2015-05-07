#FLM: Selected Glyphs Combinations Generator - Generates TXT space separated

# Description:
# Generates a txt file containing all combinations of the selected glyphs
# Can be copy-pasted to the metrics windows

# Credits:
# Pablo Impallari
# http://www.impallari.com

# Dependencies
import os.path
from robofab.world import CurrentFont

# Get current Font
f = CurrentFont()

# Get the selected characters
list = f.selection
items = len(list)

#Do some work
print "Working..."
path = f.path
dir, fileName = os.path.split(path)

output = open(dir+'/mytext.txt', 'w')

for a in list:
	for b in list:
		output.write( '/'+a+'/'+b)
		output.write( '/space')

output.close()

print "Done!"
