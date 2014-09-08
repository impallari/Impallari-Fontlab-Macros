#FLM: Sincronize Spacing Widths

# Description:
# Copy /space width to /uni00A0 and /CR glyphs
# For each font, in ALL open fonts

# Credits:
# Pablo Impallari
# http://www.impallari.com

# Dependencies
from robofab.world import AllFonts

# Clear Output windows
from FL import *
fl.output=""

# For Each font
for f in AllFonts():
	
	# Get the /space width
	myValue = f['space'].width
	
	# Apply it to other glyphs
	f['uni00A0'].width = myValue
	f['CR'].width = myValue

	f.update()

print 'done';