#FLM: Select .ss05 glyphs

# Description:
# Select all .ss05 glyphs

# Credits:
# Pablo Impallari
# http://www.impallari.com

for glyph in fl.font.glyphs:
	g = glyph.name
	if ( '.ss05' in g) : fl.Select( glyph.index )