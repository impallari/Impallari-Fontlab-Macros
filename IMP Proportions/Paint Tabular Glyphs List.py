#FLM: Paint Tabular Glyph List

# Description:
# Assuming that the default number style is tabular, 
# select all other glyphs that should also be tabular

# Credits:
# Pablo Impallari
# http://www.impallari.com


full = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'dollar', 'sterling', 'Euro', 'yen', 'cent', 'numbersign', 'paragraph', 'section', 'degree', 'percent', 'slash', 'underscore', 'plus', 'minus', 'divide', 'equal', 'multiply', 'less', 'greater', 'plusminus', 'colonmonetary', 'uni20A9', 'franc', 'uni20A6', 'lira', 'uni20BA', 'uni20B9', 'florin', 'approxequal', 'notequal', 'lessequal', 'greaterequal'];

half = ('quotedbl', 'quotesingle', 'period', 'comma', 'colon', 'semicolon', 'periodcentered', 'bar' );

f=fl.font
glyphs = f.glyphs

for item in full:
	if f.has_key(item):
		f[item].mark=100

for item in half:
	if f.has_key(item):
		f[item].mark=200

fl.UpdateFont()
		
print "Done!"