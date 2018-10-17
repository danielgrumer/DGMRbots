#MenuTitle: Adjust the proportions of comps
# -*- coding: utf-8 -*-
# made for the small caps.

import GlyphsApp

Font = Glyphs.font
selectedGlyphs = [ x.parent for x in Font.selectedLayers ]

ProportionsLight = (0.91, 0, 0, 0.86, 0, 0)
ProportionsBold = (0.94, 0, 0, 0.88, 0, 0)


def process( thisGlyph ):
	thisGlyph.layers[0].components[0].transform = ProportionsLight
	thisGlyph.layers[1].components[0].transform = ProportionsBold
	
			
Font.disableUpdateInterface()

for thisGlyph in selectedGlyphs:
	process( thisGlyph )

Font.enableUpdateInterface()

print "I'm done"