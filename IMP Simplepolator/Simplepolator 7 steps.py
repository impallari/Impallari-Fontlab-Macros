#FLM: Simplepolator 7 steps

# Simplepolator v1.1

# Description:
# A simple macro to interpolate compatible glyphs inside FontLab.
# To easily apply the Gunnlaugur SE Briem's method
# http://66.147.242.192/~operinan/2/2.3.3a/2.3.3.02.tests.htm

# Credits:
# Pablo Impallari
# http://www.impallari.com/projects/overview/simplepolation



from robofab.world import CurrentFont
from robofab.interface.all.dialogs import Message
f = CurrentFont()

if fl.count_selected != 2:
	
	Message("Select 2 glyphs for Simplepolation")	

else:	
	
	source1 = f.selection[0]
	source2 = f.selection[1]
	
	if f[source1].isCompatible(f[source2], False):

		f["interpolation.1"] = f[source1]
		f["interpolation.1"].mark = 80
		
		f["interpolation.2"].interpolate(0.16666, f[source1], f[source2])
		f["interpolation.2"].round()
		f["interpolation.2"].mark = 80
		
		f["interpolation.3"].interpolate(0.33333, f[source1], f[source2])
		f["interpolation.3"].round()
		f["interpolation.3"].mark = 80
	 
		f["interpolation.4"].interpolate(0.50, f[source1], f[source2])
		f["interpolation.4"].round()
		f["interpolation.4"].mark = 80
	
		f["interpolation.5"].interpolate(0.66666, f[source1], f[source2])
		f["interpolation.5"].round()
		f["interpolation.5"].mark = 80

		f["interpolation.6"].interpolate(0.83333, f[source1], f[source2])
		f["interpolation.6"].round()
		f["interpolation.6"].mark = 80

		f["interpolation.7"] = f[source2]
		f["interpolation.7"].mark = 80
		
		f.update()
	
	else:
	
		Message("Glyphs not compatible")
