#FLM: Select .ss03 glyphs

# Description:
# Select all .ss03 glyphs

# Credits:
# Pablo Impallari
# http://www.impallari.com

for glyph in fl.font.glyphs:
	g = glyph.name
	if ( '.ss03' in g) : fl.Select( glyph.index )