#FLM: Export Unicode List

# Description:
# Export a TXT file listing all ENCODED glyphs in the current font
# UNENCODED glyphs will be ignored

# Credits:
# Pablo Impallari1
# http://www.impallari.com

# Dependencies
import os.path
from FL import *
from robofab.world import CurrentFont
from robofab.interface.all.dialogs import PutFile

# Clear output window
fl.output=""

# Get font
font = CurrentFont()
mylist = []

# Get Encoded Glyphs
for glyph in font:
	if glyph.unicode != None:
		mylist.append('%04x' % ord(unichr(glyph.unicode)))

# Sort List
mylist = sorted(mylist)

# Save File
path = PutFile('Save file as:')
if path:
    file = open(path, 'w')
    file.write(str(mylist))
    file.close()
    
# Done!
print "Done!"