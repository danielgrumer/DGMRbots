#MenuTitle: Flip Side Bearings
# -*- coding: utf-8 -*-

__doc__="""
Flip Side Bearings for Selected Glyph
"""

import GlyphsApp

Font = Glyphs.font

selectedGlyphs = [ x.parent for x in Font.selectedLayers ]

def process(thisGlyph):
	# go over all the layers
	for l in range(len(thisGlyph.layers)):
		R = thisGlyph.layers[l].RSB
		L = thisGlyph.layers[l].LSB
		
		thisGlyph.layers[l].RSB = L
		thisGlyph.layers[l].LSB = R
						
Font.disableUpdateInterface()
				
for thisGlyph in selectedGlyphs:
	print "Processing", thisGlyph.name
	process(thisGlyph)

Font.enableUpdateInterface()

print "I'm done"
