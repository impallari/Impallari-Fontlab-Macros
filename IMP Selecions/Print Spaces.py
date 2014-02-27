#FLM: Print Selection Spaces

# Description:
# Print slected glyph names separated with spaces to the ouput windows 

# Credits:
# Pablo Impallari
# http://www.impallari.com

from robofab.world import CurrentFont

font = CurrentFont()
selection = font.selection
selection.sort()
print " ".join(selection)