#FLM: Export Lower2Lower pairs

# Description:
# Export a list of kernign pairs, to be used in the Contextual Kerning tool
# 
# It only reports MAIN pairs (ie. those using classes)
# If you want ALL pairs, run this macro on a copy of your font having the kerning manually expanded
#
# Pablo Impallari
# http://www.impallari.com

uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Clear Output windows
from FL import *
fl.output=""

# Dependencies
from robofab.world import AllFonts, CurrentFont
import os.path

f = CurrentFont()
kerning = f.kerning

path = f.path
dir, fileName = os.path.split(path)

print 'Inspecting ' + str(f.info.familyName) + ' ' + str(f.info.styleName) + '...'

#Get Lower to Lower
print "Searching for Lower to Lower Pairs"
target = lowercase
against = lowercase
output = open(dir+'/Kern Lower to Lower.txt', 'w')

for t in target:
	i = 0
	for a in against:
		if f.kerning[(t, a)]:
				output.write( '"' + str(t) + str(a) + '", ')
				i += 1
				print str(t) + str(a)
	if (i > 0):
		output.write('\n')

output.close()
	
# Done!
print "Done!"