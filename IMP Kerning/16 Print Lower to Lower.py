#FLM: Print Lower 2 Lower Kerning Pairs

# Description:
# Print all lower to lower kerning pairs

# To-do:
# It only report main pairs, not fully expanded if the font uses classes

# Credits:
# Pablo Impallari

from robofab.world import CurrentFont

f = CurrentFont()
kerning = f.kerning

# Clear Output windows
from FL import *
fl.output=""

# List of glyphs to combine
target = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];
against = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];

# Write Combintions to the Output Windows
for t in target:
	for a in against:
		if kerning[(t,a)]:
			print t + " " + a + ": " + str(kerning[(t,a)])

print "Done!"