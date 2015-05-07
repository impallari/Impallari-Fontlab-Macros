#FLM: Print all Kerning Pairs for the current font

# Description:
# Print all Kerning Pairs for the current font

# Dependencies
from robofab.world import CurrentFont

# Clear Output windows
from FL import *
fl.output=""

# Get Kerning Values
f = CurrentFont()
kerning = f.kerning

# Print all Pairs
for (left, right), value in kerning.items():
    print left, right, value  

print "Done!"