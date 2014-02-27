#FLM: 01 Check that all glyphs are present

# Description:
# Checks that all needed glyphs are present

# Credits:
# Pablo Impallari
# http://www.impallari.com

print "Starting..."

# Glyphs Needed to generate all the Diacritics
Caps = ['A', 'AE', 'C', 'D', 'E', 'G', 'H', 'I', 'J', 'K', 'L', 'N', 'O', 'Oslash', 'R', 'S', 'T', 'U', 'V', 'Y', 'Z'];
Lower = ['a', 'ae', 'c', 'd', 'e', 'g', 'h', 'dotlessi', 'dotlessj', 'k', 'l', 'm', 'n', 'o', 'oslash', 'r', 's', 't', 'u', 'w', 'y', 'z'];
Marks = ['acute', 'apostrophe', 'breve', 'caron', 'caron.alt', 'cedilla', 'circumflex', 'commaaccent', 'dieresis', 'dotaccent', 'dotbelow', 'grave', 'hungarumlaut', 'macron', 'ogonek', 'ring', 'tilde', 'uni030F', 'uni0311', 'periodcentered', 'acute.cap', 'breve.cap', 'caron.cap', 'circumflex.cap', 'dieresis.cap', 'dotaccent.cap', 'grave.cap', 'hungarumlaut.cap', 'macron.cap', 'ring.cap', 'tilde.cap', 'uni030F.cap', 'uni0311.cap'];

# Get the Font
f=fl.font

missingCount = 0

# Check
for item in Caps:
	if not f.has_key(item):
		print item + ' is missing';
		missingCount += 1

for item in Lower:
	if not f.has_key(item):
		print item + ' is missing';
		missingCount += 1
		
for item in Marks:
	if not f.has_key(item):
		print item + ' is missing';	
		missingCount += 1	

if missingCount == 0:
	print "All needed glyphs are present!"

else:
	print str(missingCount) + ' Glyphs missing'
	
print "Done!"



