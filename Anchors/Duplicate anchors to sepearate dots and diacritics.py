#MenuTitle: Arabic | Duplicate anchors to separate dots and diacritics
# -*- coding: utf-8 -*-

import GlyphsApp

f = Glyphs.font
selectedGlyphs = [ x.parent for x in f.selectedLayers ]
		
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
			thisGlyph.layers[layer].anchors['top'].y = yy + 100
			
		if anchor.name == "bottom": 
			print thisGlyph.name, "bottom"
			anchor.name = "bottomDots"
			
			thisGlyph.layers[layer].anchors['bottom'] = GSAnchor() 
			thisGlyph.layers[layer].anchors['bottom'].x = xx
			thisGlyph.layers[layer].anchors['bottom'].y = yy - 100
			
		
Font.disableUpdateInterface()

for thisGlyph in selectedGlyphs:
	process(thisGlyph, 0)
	process(thisGlyph, 1)

for feature in f.features:
        if feature.automatic:
                feature.update()

Font.enableUpdateInterface()


# print "I'm done"