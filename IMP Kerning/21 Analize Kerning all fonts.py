#FLM: Analize Kerning Pairs in from all open Fonts

# Description:
# Count the occurence of kerning pairs across all open fonts

# Credits:
# Pablo Impallari1
# http://www.impallari.com

# Level of coincindence ( 1 to 100 )
# Example: 50 means: Pairs appearing in more than 50% of all the open fonts
percentaje = 60

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
output = open(dir+'/Kern-Analisis.txt', 'w')

# Get count of all open fonts
mytotal = sum(f.info.familyName != "" for f in AllFonts())
thresold = percentaje * mytotal / 100
print "Open Fonts: " + str(mytotal)
print "Searching for Kerning Pairs precent in more than " + str(thresold) + " fonts"

# Initialize Values all set to Zero
for f in AllFonts():
	print 'Analizing ' + str(f.info.familyName) + ' ' + str(f.info.styleName) + '...'
	kerning = f.kerning
	for (left, right), value in kerning.items():
		try:
			results[left][right] += 1 
		except:
			results[left][right] = 0 

print ''
		
# Print Results
for l,r in results.iteritems(): # will become d.items() in py3k
	for r,v in r.iteritems(): # will become d.items() in py3k
		if v >= thresold:
			output.write( str(l)+'; '+str(r)+'; '+str(v))
			output.write( '\n')

output.close()	
# Done!
print "Done!"