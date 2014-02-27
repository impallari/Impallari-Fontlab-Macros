#FLM: Simplepolator 10 steps

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

interpolationSteps = 10 - 1
extrapolateSteps = 5

startColor = 50
endColor = 120

if fl.count_selected != 2:
	
	Message("Select 2 glyphs for Simplepolation")	

else:	
	
	source1 = f.selection[0]
	source2 = f.selection[1]
	
	if f[source1].isCompatible(f[source2], False):
	
		nameSteps = 1
		for i in range(-extrapolateSteps, interpolationSteps + extrapolateSteps + 1, 1):

			name = "interpolation.%03i" % nameSteps
			factor = i / float(interpolationSteps)
			color = int(startColor + (endColor - startColor) * factor)

			# print str(factor)        

			f[name].interpolate(factor, f[source1], f[source2])
			f[name].round()
			
			if (factor < 0):
				f[name].mark = 161
			elif (factor > 1):
				f[name].mark = 245
			else:
				f[name].mark = color
			
			nameSteps += 1   
		
		f.update()
	
	else:
	
		Message("Glyphs not compatible")
