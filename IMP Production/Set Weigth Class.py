#FLM: Set WeightClass

# Description:
# Set WeightClass according to postscriptWeightName
# For each font, in ALL open fonts
# This macro assumes my own naming scheme - Tweakit to use your own!

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
	print f.info.familyName
	print f.info.postscriptWeightName
	print "Old WeightClass: " + str(f.info.openTypeOS2WeightClass)

	old = f.info.openTypeOS2WeightClass
	
	if f.info.postscriptWeightName == "Thin":
		f.info.openTypeOS2WeightClass = 250
		
	if f.info.postscriptWeightName == "ExtraLight":
		f.info.openTypeOS2WeightClass = 275
		
	if f.info.postscriptWeightName == "Light":
		f.info.openTypeOS2WeightClass = 300	
		
	if f.info.postscriptWeightName == "Regular":
		f.info.openTypeOS2WeightClass = 325
		
	if f.info.postscriptWeightName == "Medium":
		f.info.openTypeOS2WeightClass = 350
		
	if f.info.postscriptWeightName == "SemiBold":
		f.info.openTypeOS2WeightClass = 400
		
	if f.info.postscriptWeightName == "Bold":
		f.info.openTypeOS2WeightClass = 450
		
	if f.info.postscriptWeightName == "ExtraBold":
		f.info.openTypeOS2WeightClass = 475
		
	if f.info.postscriptWeightName == "Black":
		f.info.openTypeOS2WeightClass = 500
	
	print "New WeightClass: " + str(f.info.openTypeOS2WeightClass)
	print ""
	
	f.update()

print 'done';