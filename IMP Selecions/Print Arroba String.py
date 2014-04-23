#FLM: Print Arroba String for Preview Windows

# Description:
# Print arroba string using selected glyphs

# Credits:
# Pablo Impallari
# http://www.impallari.com

from robofab.world import CurrentFont

f = CurrentFont()

# Get the selected characters
list = f.selection
items = len(list)

cadena = "/espaciador @/espaciador "

for a in list:
	cadena = cadena + " /" + a + " @/" + a + " "
	
print cadena
