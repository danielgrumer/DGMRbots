#MenuTitle: Copy Stuff | From one's master to another's background
# -*- coding: utf-8 -*-

import GlyphsApp

Font = Glyphs.font
selectedGlyphs = [ x.parent for x in Font.selectedLayers ]
import copy

INPUTLAYER = 1
OUTPUTLAYERS = [1]

ALL = {
	"paths"      : True,
	"components" : True,
	"anchors"    : False,
	"guides"     : False,
	"width"      : False,
	}

def process( thisGlyph ):
 	IN = thisGlyph.layers[INPUTLAYER]

 	for layer in OUTPUTLAYERS:
		OUT = thisGlyph.layers[layer].background

 		if ALL["paths"]:
			OUT.paths = []

 		if ALL["components"]:
 			OUT.components = []

		for i in ALL:
			if ALL[i] :
				if (IN.i):
					OUT.i = copy.copy(IN.i)
			else:
				print "skipped ", i

Font.disableUpdateInterface()
for thisGlyph in selectedGlyphs:
	process( thisGlyph )
Font.enableUpdateInterface()

print "I'm done"