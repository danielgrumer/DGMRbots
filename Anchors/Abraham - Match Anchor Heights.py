#MenuTitle: Abraham | Match Anchor Heights
# -*- coding: utf-8 -*-
__doc__="""
Match Anchor Heights
"""

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
#		- use the MASTERLAYER from the selected layer
#		- interface
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Font = Glyphs.font
selectedGlyphs = [ x.parent for x in Font.selectedLayers ]


MASTERLAYER = 2
TARGETS = [
	"top", 
	"top_1", 
	"top_2", 
	"bottom", 
	"bottom_1", 
	"bottom_2",
	]

def process( thisGlyph ):
	print thisGlyph.name
	
	AMOUNT = len(thisGlyph.layers[MASTERLAYER].anchors)
	
	for j in range(len(thisGlyph.layers)):
		for anchor in thisGlyph.layers[j].anchors:
			if anchor.name in TARGETS:
				src = anchor.y
				dst = thisGlyph.layers[MASTERLAYER].anchors[anchor.name].y
				if src != dst:	
					anchor.y = dst
					print anchor.name, j+1, src, ">>", dst

for thisGlyph in selectedGlyphs:
	process( thisGlyph )


