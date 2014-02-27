#FLM: Generate Pair list for Metrics Machine

# Description:
# Create a custom pair list for Metrics Machine

# Credits:
# Pablo Impallari1
# http://www.impallari.com

#Dependencies
import os.path
from robofab.world import CurrentFont

# Configuration
titulo = "New M pairs"
first_list = ['M'];
second_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];

# Get current Font
f = CurrentFont()

#Do some work
print "Working..."
path = f.path
dir, fileName = os.path.split(path)

output = open(dir+'/'+titulo+'.txt', 'w')

output.write( "#KPL:P: " + titulo )
output.write( '\n')
print "#KPL:P: " + titulo

count = 0
for first in first_list:
	for second in second_list:
		output.write( first + " " + second)
		output.write( '\n')
		print first + " " + second
		count = count + 1

print count
print "Done!"

