#FLM: Print Selection in New Lines

# Description:
# Print selected glyph names separated with new lines to the ouput windows 

# Credits:
# Pablo Impallari
# http://www.impallari.com

from robofab.world import CurrentFont

font = CurrentFont()
selection = font.selection
# selection.sort()
print "\n".join(selection)