#FLM: Print Selection formated for Python List

# Description:
# Print slected glyph names, formated to be included in python lists

# Credits:
# Pablo Impallari
# http://www.impallari.com

from robofab.world import CurrentFont

font = CurrentFont()
selection = font.selection
selection.sort()

print "'" + "', '".join(selection) + "'"

# print "'"
# print "', '".join(selection)
# print "'"