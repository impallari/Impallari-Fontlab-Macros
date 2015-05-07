#FLM: Analize Kerning Pairs in from all open Fonts

# Description:
# Count the occurence of kerning pairs across all open fonts

# Credits:
# Pablo Impallari1
# http://www.impallari.com

# Clear Output windows
from FL import *
fl.output=""

# Dependencies
from robofab.world import AllFonts, CurrentFont
from collections import defaultdict
import os.path

# Variables
tree = lambda: defaultdict(tree)
results = tree()

#Get Path to write the results
f = CurrentFont()
path = f.path
dir, fileName = os.path.split(path)
output = open(dir+'/Kern-Analisis.csv', 'w')

# Initialize Values all set to Zero
for f in AllFonts():
	kerning = f.kerning
	for (left, right), value in kerning.items():
		results[left][right] = 0 

# Now count again, this time adding 1 for each occureence
for f in AllFonts():
	print 'Analizing ' + str(f.info.familyName) + ' ' + str(f.info.styleName) + '...'
	kerning = f.kerning
	for (left, right), value in kerning.items():
		results[left][right] += 1

print ''
		
# Print Results
for l,r in results.iteritems(): # will become d.items() in py3k
	for r,v in r.iteritems(): # will become d.items() in py3k
		output.write( str(l)+'; '+str(r)+'; '+str(v))
		output.write( '\n')

output.close()	
# Done!
print "Done!"