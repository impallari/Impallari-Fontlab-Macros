#FLM: Select .ss02 glyphs

# Description:
# Select all .ss02 glyphs

# Credits:
# Pablo Impallari
# http://www.impallari.com

for glyph in fl.font.glyphs:
	g = glyph.name
	if ( '.ss02' in g) : fl.Select( glyph.index )