#FLM: Select .ss04 glyphs

# Description:
# Select all .ss04 glyphs

# Credits:
# Pablo Impallari
# http://www.impallari.com

for glyph in fl.font.glyphs:
	g = glyph.name
	if ( '.ss04' in g) : fl.Select( glyph.index )