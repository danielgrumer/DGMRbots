#MenuTitle: Find and Repalce Y values
# -*- coding: utf-8 -*-

__doc__="""
Find and Replace in Anchor Names
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
#		- Rainer did it, probably better.
#
#	_TODO:
#		- interface
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


import GlyphsApp

Font = Glyphs.font
selectedGlyphs = [ x.parent for x in Font.selectedLayers ]

# ---------------- #

# Y values to find
FIND = [690, -10]

# Y values to replace
REPLACE = [684, -12]

# ---------------- #

def replace(WHO):
	for i in range(len(FIND)):
		if (WHO.y == FIND[i]):
			print thisGlyph.name, WHO.y, i
			WHO.y = REPLACE[i]
			print WHO.y
		
def process(thisGlyph):
	# go over all the layers
	for layer in range(len(thisGlyph.layers)):
		
		# go over all the paths
		for path in thisGlyph.layers[layer].paths:
			# go over all noes
			for node in path.nodes:
				replace(node)		
		
		# go over all the anchors
		for anchor in thisGlyph.layers[layer].anchors:
			replace(anchor)

					

				
Font.disableUpdateInterface()
				
for thisGlyph in selectedGlyphs:
	print "Processing", thisGlyph.name
	process(thisGlyph)

Font.enableUpdateInterface()

print "I'm done"

