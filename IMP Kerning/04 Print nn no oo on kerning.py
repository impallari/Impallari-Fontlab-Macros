#FLM: Print nn no oo on kerning pairs

# Description:
# Print nn no oo on kerning pairs values

# To-do:
# It only report main pairs, not fully expanded if the font uses classes

# Credits:
# Pablo Impallari

# Dependencies
from robofab.world import CurrentFont

# Clear Output windows
from FL import *
fl.output=""

# Get Kerning
f = CurrentFont()
kerning = f.kerning

# Print n n
if kerning[('n','n')]:
	print "n n: " + str(kerning[('n','n')])

# Print n o
if kerning[('n','o')]:
	print "n o: "  + str(kerning[('n','o')])

# Print o o
if kerning[('o','o')]:
	print "o o: " + str(kerning[('o','o')])

# Print o n
if kerning[('o','n')]:
	print "o n: " + str(kerning[('o','n')])

print "Done!"