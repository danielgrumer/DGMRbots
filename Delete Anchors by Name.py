#MenuTitle: Anchors | Remove Anchors by name
# -*- coding: utf-8 -*-
__doc__="""
Remove Anchors by name
"""

import GlyphsApp

Font = Glyphs.font
selectedGlyphs = [ x.parent for x in Font.selectedLayers ]

# ---------------- #

# Yanek, Here you should write the name of the anchor you want to delete"
TARGET = 'AnchorName'

# ---------------- #


def process(thisGlyph):
	# go over all the layers
	for l in range(len(thisGlyph.layers)):
		for i in thisGlyph.layers[l].anchors:
			if (TARGET == i.name):
				del thisGlyph.layers[l].anchors[TARGET]
				print "Removed", TARGET, "from", thisGlyph.name, "Master Number", l+1
				break
				
Font.disableUpdateInterface()
				
for thisGlyph in selectedGlyphs:
	print "Processing", thisGlyph.name
	process(thisGlyph)

Font.enableUpdateInterface()

print "I'm done"

