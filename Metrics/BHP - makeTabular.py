#MenuTitle: BHP | Make Tabular
# -*- coding: utf-8 -*-

import GlyphsApp

Font = Glyphs.font
selectedGlyphs = [ x.parent for x in Font.selectedLayers ]

def process( thisGlyph ):
	NAME = str(thisGlyph.name)
	NAME = NAME.strip(".tf")
		
 	for l in range(len(thisGlyph.layers)):
 		thisGlyph.layers[l].paths = []
  		
  		thisGlyph.layers[l].components = []
  		thisGlyph.layers[l].components.append(GSComponent(NAME))
  		thisGlyph.layers[l].width = 500
  		
  		SB = thisGlyph.layers[l].LSB + thisGlyph.layers[l].RSB
 		thisGlyph.layers[l].LSB = SB/2
  		thisGlyph.layers[l].width = 500
 		
 		
Font.disableUpdateInterface()
for thisGlyph in selectedGlyphs:
	process( thisGlyph )
Font.enableUpdateInterface()

print "I'm done"