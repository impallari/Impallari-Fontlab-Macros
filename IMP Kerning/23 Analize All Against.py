#FLM: Analize All Against

# Description:
# Count the occurence of kerning pairs across all open fonts
# But only for the glyphs listed in the "target" against "against" variables

# Credits:
# Pablo Impallari1
# http://www.impallari.com

uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
punctuation = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['eight', 'five', 'four', 'nine', 'one', 'seven', 'six', 'three', 'two', 'zero']

target = uppercase
against = uppercase
percentaje = 50 # Example: 50 = Pairs appearing in more than 50% of the open fonts

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
output = open(dir+'/Kern Cap to Cap.txt', 'w')
#output = open(dir+'/Kern Cap to Lower.txt', 'w')
#output = open(dir+'/Kern Cap to Punctuation.txt', 'w')
#output = open(dir+'/Kern Lower to Lower.txt', 'w')
#output = open(dir+'/Kern Lower to Punctuation.txt', 'w')
#output = open(dir+'/Kern Punctuation to Cap', 'w')
#output = open(dir+'/Kern Punctuation to Lower.txt', 'w')
#output = open(dir+'/Kern Numbers to Numbers.txt', 'w')


# Get count of all open fonts
mytotal = sum(f.info.familyName != "" for f in AllFonts())
thresold = percentaje * mytotal / 100
print "Open Fonts: " + str(mytotal)
print "Searching for Kerning Pairs precent in more than " + str(thresold) + " fonts"

# Initialize Values all set to Zero
for f in AllFonts():
	print 'Inspecting ' + str(f.info.familyName) + ' ' + str(f.info.styleName) + '...'
	kerning = f.kerning
	for t in target:
		for a in against:
			if f.kerning[(t, a)]:
					results[t][a] = 0 
					# print t + " " + a

# Now count again, this time adding 1 for each occureence
for f in AllFonts():
	print 'Analizing ' + str(f.info.familyName) + ' ' + str(f.info.styleName) + '...'
	kerning = f.kerning
	for t in target:
		for a in against:
			if f.kerning[(t, a)]:
					results[t][a] += 1
					# print t + " " + a

print ''
		
# Print Results
for l,r in results.iteritems(): # will become d.items() in py3k
	for r,v in r.iteritems(): # will become d.items() in py3k
		if v >= thresold:
			output.write( str(l)+'; '+str(r)+'; '+str(v))
			# output.write( 'HH' + str(l) + str(r) + 'HH OO' + str(l) + str(r) + 'OO')
			# output.write( 'oo' + str(l) + str(r) + 'oo nn' + str(l) + str(r) + 'nn')
			output.write( '\n')

output.close()	
# Done!
print "Done!"