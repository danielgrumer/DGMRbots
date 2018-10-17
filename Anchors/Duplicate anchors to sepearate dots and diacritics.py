#MenuTitle: Arabic | Duplicate anchors to separate dots and diacritics
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
#		- Make it work on all layers or a selected layer
#		- interface to set the DELTA
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import GlyphsApp

f = Glyphs.font
selectedGlyphs = [ x.parent for x in f.selectedLayers ]
	
DELTA = 100

def process(thisGlyph, layer):
	for anchor in thisGlyph.layers[layer].anchors:
		xx = anchor.x
		yy = anchor.y		
		print anchor
		if anchor.name == "top":
			print thisGlyph.name, "top"

			anchor.name = "topDots"
			
			thisGlyph.layers[layer].anchors['top'] = GSAnchor() 
			thisGlyph.layers[layer].anchors['top'].x = xx
			thisGlyph.layers[layer].anchors['top'].y = yy + DELTA
			
		if anchor.name == "bottom": 
			print thisGlyph.name, "bottom"
			anchor.name = "bottomDots"
			
			thisGlyph.layers[layer].anchors['bottom'] = GSAnchor() 
			thisGlyph.layers[layer].anchors['bottom'].x = xx
			thisGlyph.layers[layer].anchors['bottom'].y = yy - DELTA
			
		
Font.disableUpdateInterface()

for thisGlyph in selectedGlyphs:
	process(thisGlyph, 0)
	process(thisGlyph, 1)

for feature in f.features:
        if feature.automatic:
                feature.update()

Font.enableUpdateInterface()


# print "I'm done"