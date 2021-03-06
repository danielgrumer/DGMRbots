#MenuTitle: Zico Display | Update the 3rd master to match the 4th
# -*- coding: utf-8 -*-

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#	Version: 0.1
#
#	>> Daniel Grumer
#	>> www.danielgrumer.com <<
#
#	_NOTES:
#		- 
#
#	_TODO:
#		- make one good Copier script
#		- interface. select input layer, output layer(s), checkboxes, and support background too.
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import GlyphsApp

Font = Glyphs.font
selectedGlyphs = [ x.parent for x in Font.selectedLayers ]
import copy

INPUTLAYER = 2
OUTPUTLAYERS = [0,1,3]

def process( thisGlyph ):
 	IN = thisGlyph.layers[INPUTLAYER]

 	for layer in OUTPUTLAYERS:
	 	OUT = thisGlyph.layers[layer]
		OUT.paths = []
 		OUT.components = []

 		if (IN.paths):
 			OUT.paths = copy.copy(IN.paths)

 		if (IN.components):
			OUT.components = copy.copy(IN.components)
		
		OUT.guides = copy.copy(IN.guides)
		
 		if (IN.anchors):
			OUT.anchors = copy.copy(IN.anchors)
#		OUT.width = IN.width

Font.disableUpdateInterface()
for thisGlyph in selectedGlyphs:
	process( thisGlyph )
Font.enableUpdateInterface()

print "I'm done"