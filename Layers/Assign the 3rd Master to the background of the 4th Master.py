#MenuTitle: Zico Display | Assign the 3rd Master to the background of the 4th Master
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