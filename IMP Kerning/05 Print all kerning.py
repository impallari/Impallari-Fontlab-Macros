#FLM: Print all Kerning Pairs

# Description:
# Print all Kerning Pairs


from robofab.world import CurrentFont

f = CurrentFont()
kerning = f.kerning

# this prints all the pairs
for (left, right), value in kerning.items():
    print (left, right), value  

print "Done!"