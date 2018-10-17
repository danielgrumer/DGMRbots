#MenuTitle: Abraham | Make sure anchors are consistent
# -*- coding: utf-8 -*-
__doc__="""
Make sure anchors are consistent
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
#		- use the EXAMPLE from the selected layer
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Font = Glyphs.font
selectedGlyphs = [ x.parent for x in Font.selectedLayers ]

EXAMPLE = 2

def process( thisGlyph ):
	print thisGlyph.name
	
	AMOUNT = len(thisGlyph.layers[EXAMPLE].anchors)
	
	for j in range(len(thisGlyph.layers)):
		if (len(thisGlyph.layers[j].anchors) != AMOUNT):
			print "problem in Master No.", j+1
			matchAnchors(thisGlyph, j)
			

def matchAnchors(thisGlyph, layer):
	names = collectNames(thisGlyph, EXAMPLE)
	mynames = collectNames(thisGlyph, layer)

	for anchor in thisGlyph.layers[layer].anchors:
		if anchor.name not in names:
 			del thisGlyph.layers[layer].anchors[anchor.name]
			print "Removed", anchor.name, "from", thisGlyph.name, "Master Number", layer+1

 	for nom in names:
 		if nom not in mynames:
 			newAnchor = GSAnchor()
			newAnchor.name = nom
			newAnchor.position = thisGlyph.layers[EXAMPLE].anchors[nom].position
 			thisGlyph.layers[layer].addAnchor_( newAnchor )
 			print "Added", nom, "to", thisGlyph.name, "Master Number", layer+1

def collectNames(thisGlyph, layer):
	mylist = []
	for anchor in thisGlyph.layers[layer].anchors:
		mylist.append(anchor.name)
	return mylist

for thisGlyph in selectedGlyphs:
	process( thisGlyph )
