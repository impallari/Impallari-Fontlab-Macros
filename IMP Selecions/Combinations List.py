#FLM: List fo Glyphs Combinations Generator - Print combinations

# Description:
# Generate combination between 2 lists of glyphs
# Usefull for Spacing, Kerning, etc...

# Credits:
# Idea by Yorlmar Campos - http://www.rnsfonts.com
# Coding by Pablo Impallari - http://www.impallari.com

# List of glyphs to combine, tweak as needed
target = ['/A','/A.ss01','/A.ss02'];
against = ['/H','/O'];

# Clear Output windows
from FL import *
fl.output=""

# Write Combintions to the Output Windows
results = ""

for t in target:
	for a in against:
		results += str(a + t + a)
		
print results

# Done
print "Done!"