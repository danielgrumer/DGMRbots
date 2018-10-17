#MenuTitle: Abraham | Interpolate Sidebearings
# -*- coding: utf-8 -*-

# A script that updates the 3rd master according to the 4th

import GlyphsApp

Font = Glyphs.font
selectedGlyphs = [ x.parent for x in Font.selectedLayers ]

def process( thisGlyph, r, l ):
 	THIN = thisGlyph.layers[0]
 	LIGHT = thisGlyph.layers[1]
 	BOLD = thisGlyph.layers[2]
 	BLACK = thisGlyph.layers[3]

 	print thisGlyph.name

 	if (l == True):
	 	LIGHT.LSB = THIN.LSB + 0.2 * (BLACK.LSB - THIN.LSB)
	 	BOLD.LSB = THIN.LSB + 0.8 * (BLACK.LSB - THIN.LSB)
	 	print "left", THIN.LSB, LIGHT.LSB, BOLD.LSB, BLACK.LSB

	if (r == True):
	 	LIGHT.RSB = THIN.RSB + 0.2 * (BLACK.RSB - THIN.RSB)
	 	BOLD.RSB = THIN.RSB + 0.8 * (BLACK.RSB - THIN.RSB)
	 	print "right", THIN.RSB, LIGHT.RSB, BOLD.RSB, BLACK.RSB

 	print "-----"

Font.disableUpdateInterface()
for thisGlyph in selectedGlyphs:
	if "fina" in thisGlyph.name:
		process( thisGlyph, False, True)

	elif "medi" in thisGlyph.name:
		process( thisGlyph, False, False)

	elif "init" in thisGlyph.name:
		process( thisGlyph, True, False)

	else:
		process( thisGlyph, True, True)

Font.enableUpdateInterface()

print "I'm done"