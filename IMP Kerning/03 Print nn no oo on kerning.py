#FLM: Print nn no oo on kerning pairs

# Description:
# Print nn no oo on kerning pairs

# Credits:
# Pablo Impallari

from robofab.world import CurrentFont

f = CurrentFont()
kerning = f.kerning

if kerning[('n','n')]:
	print "n n: " + str(kerning[('n','n')])

if kerning[('n','o')]:
	print "n o: "  + str(kerning[('n','o')])

if kerning[('o','o')]:
	print "o o: " + str(kerning[('o','o')])

if kerning[('o','n')]:
	print "o n: " + str(kerning[('o','n')])


print "Done!"