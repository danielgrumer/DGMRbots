#MenuTitle: Hadassah Arabic | Compare Comps between Masters 0 and 1
# -*- coding: utf-8 -*-

import GlyphsApp

Font = Glyphs.font
selectedGlyphs = [ x.parent for x in Font.selectedLayers ]

def process( thisGlyph ):
 	COMPS1 = []
 	for comp in thisGlyph.layers[1].components:
 		COMPS1.append(str(comp.componentName))

 	COMPS2 = []
 	for comp in thisGlyph.layers[0].components:
 		COMPS2.append(str(comp.componentName))
 	
 	if cmp(COMPS1, COMPS2) != 0:
 		print thisGlyph.name

Font.disableUpdateInterface()
for thisGlyph in selectedGlyphs:
	process( thisGlyph )
Font.enableUpdateInterface()

print "I'm done"