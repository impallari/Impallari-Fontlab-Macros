#FLM: Kerning Combinations Generator

# Description:
# Generate combination between list of glyphs
# Usefull for Spacing, Kerning, etc...

# Credits:
# Idea by Yorlmar Campos - http://www.rnsfonts.com
# Coding by Pablo Impallari - http://www.impallari.com

# Clear Output windows
from FL import *
fl.output=""

# List of glyphs to combine
target = ['/A','/A.ss01','/A.ss02'];
against = ['/H','/O'];

results = ""

# Write Combintions to the Output Windows
for t in target:
	for a in against:
		results += str(a + t + a)

print results

# Done
print "Done!"