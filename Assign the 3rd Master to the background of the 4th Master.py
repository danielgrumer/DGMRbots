#MenuTitle: Zico Display | Assign the 3rd Master to the background of the 4th Master
# -*- coding: utf-8 -*-

# A script that updates the 3rd master according to the 4th

import GlyphsApp

Font = Glyphs.font
selectedGlyphs = [ x.parent for x in Font.selectedLayers ]
import copy

INPUTLAYER = 2
OUTPUTLAYER = 3


def process( thisGlyph ):
 	IN = thisGlyph.layers[INPUTLAYER]
 	OUT = thisGlyph.layers[OUTPUTLAYER]

	OUT.background.paths = copy.copy(IN.paths)
# 	OUT.paths = copy.copy(IN.paths)
# 	OUT.components = copy.copy(IN.components)
	OUT.anchors = copy.copy(IN.anchors)
  	OUT.width = IN.width

Font.disableUpdateInterface()
for thisGlyph in selectedGlyphs:
	process( thisGlyph )
Font.enableUpdateInterface()

print "I'm done"