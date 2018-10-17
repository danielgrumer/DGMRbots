#MenuTitle: Delete Comps and Paths from all layers
# -*- coding: utf-8 -*-

import GlyphsApp

Font = Glyphs.font
selectedGlyphs = [ x.parent for x in Font.selectedLayers ]

def process( thisGlyph ):
	# For each layer
	for i in range(len(thisGlyph.layers)):	
		
		# If there are paths
		while len(thisGlyph.layers[i].paths) > 0:
			del( thisGlyph.layers[i].paths[0] )
				
		# If there are components
		while len(thisGlyph.layers[i].components) > 0:
			del(thisGlyph.layers[i].components[0])

Font.disableUpdateInterface()

for thisGlyph in selectedGlyphs:
	process( thisGlyph )

Font.enableUpdateInterface()