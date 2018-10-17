#MenuTitle: Brown | Interpolate Sidebearings between Thin and Black
# -*- coding: utf-8 -*-

import GlyphsApp

Font = Glyphs.font
selectedGlyphs = [ x.parent for x in Font.selectedLayers ]

def process( thisGlyph):
 	THIN = thisGlyph.layers[0]
 	REGULAR = thisGlyph.layers[1]
 	BLACK = thisGlyph.layers[2]

 	print thisGlyph.name
	
	REGULAR.LSB = (BLACK.LSB + THIN.LSB) / 2
	REGULAR.RSB = (BLACK.RSB + THIN.RSB) / 2

 	print "-----"

Font.disableUpdateInterface()
for thisGlyph in selectedGlyphs:
	process( thisGlyph)

Font.enableUpdateInterface()

print "I'm done"