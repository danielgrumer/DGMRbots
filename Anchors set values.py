#MenuTitle: Anchors | Set values for tops
# -*- coding: utf-8 -*-

# Set anchors positions 

import GlyphsApp

Font = Glyphs.font
selectedGlyphs = [ x.parent for x in Font.selectedLayers ]

# write here the top value for each master
TOPS = [ 505, 506, 509 ] 

def process( thisGlyph ):

	for l in range(len(TOPS)):		
		for i in thisGlyph.layers[l].anchors:
			if "top" in i.name:
				i.y = TOPS[l]	
			if "center" in i.name:
				i.y = TOPS[l]/2	

Font.disableUpdateInterface()
for thisGlyph in selectedGlyphs:
	process( thisGlyph )
Font.enableUpdateInterface()

print "I'm done"