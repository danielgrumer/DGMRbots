#MenuTitle: Heidenheim - Inliner - Split Offset Path Results to TWO.
# -*- coding: utf-8 -*-

# A second script for Heidenheim Inliner, to 

import GlyphsApp

Font = Glyphs.font
selectedGlyphs = [ x.parent for x in Font.selectedLayers ]
import copy

LAYER = 1

# make sure paths are selected
def detectPaths(thisGlyph):
	thisLayer = thisGlyph.layers[LAYER]
	selectedPaths = []
 	for path in thisLayer.paths:
 		for node in path.nodes:
 			if node.selected and path not in selectedPaths:
 				selectedPaths.append(path)
	if len(selectedPaths) > 0:
		return selectedPaths
	else:
		return False

def splitPath (path):
	LENGTH = len(path)
	newPath1 = GSPath()
	newPath2 = GSPath()
	
	for i in range((LENGTH/2)):
		virtualNode = GSNode()
		virtualNode.position = path.nodes[i-1].position
	 	virtualNode.connection = path.nodes[i-1].connection
		virtualNode.type = path.nodes[i-1].type 		
		newPath1.nodes.append(virtualNode)
			
	for i in range((LENGTH/2)):
		virtualNode = GSNode()
		virtualNode.position = path.nodes[i-1+LENGTH/2].position
	 	virtualNode.connection = path.nodes[i-1+LENGTH/2].connection
		virtualNode.type = path.nodes[i-1 +LENGTH/2].type 		
		newPath2.nodes.append(virtualNode)

 	thisGlyph.layers[LAYER].paths.remove( path )
 	thisGlyph.layers[LAYER].paths.append( newPath1 )
 	thisGlyph.layers[LAYER].paths.append( newPath2 )


def process(thisGlyph):
	if detectPaths(thisGlyph):
		for path in detectPaths(thisGlyph):
			# Make sure the paths are even
		 	if (len(path) % 2 ) == 0:
		 		splitPath(path)
		 	else:
		 		print "OOPS. path is not divisible by two."
	else:
	 	print "you have to select at least one path..."
	 	
Font.disableUpdateInterface()
for thisGlyph in selectedGlyphs:
	process( thisGlyph )
Font.enableUpdateInterface()

# print "I'm done"




