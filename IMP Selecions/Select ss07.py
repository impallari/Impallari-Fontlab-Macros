#FLM: Select .ss07 glyphs

# Description:
# Select all .ss07 glyphs

# Credits:
# Pablo Impallari
# http://www.impallari.com

for glyph in fl.font.glyphs:
	g = glyph.name
	if ( '.ss07' in g) : fl.Select( glyph.index )