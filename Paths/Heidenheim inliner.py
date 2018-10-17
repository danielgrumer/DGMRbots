#MenuTitle: Heidenheim - Inliner
# -*- coding: utf-8 -*-

# A script that creates the inlines for Heidenheim


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#	Version: 0.1
#
#	>> Daniel Grumer
#	>> www.danielgrumer.com <<
#
#	_NOTES:
#		- A script that creats the inlines for Heidenheim Display. 
#
#	_TODO:
#		- continue this script to (a) apply the filter, and (b) split the offset path results
#		- interface. choose number of line. 
#		- make it work on the active layer.
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


import GlyphsApp

Font = Glyphs.font
selectedGlyphs = [ x.parent for x in Font.selectedLayers ]
import copy

LAYER = 1
HOWMANYLINES = 1  

# make sure two paths are selected
def detectPaths(thisGlyph):
	thisLayer = thisGlyph.layers[LAYER]
	selectedPaths = []
 	for path in thisLayer.paths:
 		for node in path.nodes:
 			if node.selected and path not in selectedPaths:
 				selectedPaths.append(path)
	if len(selectedPaths) == 2:
		return selectedPaths
	else:
		return False

# the interpolation function
def interpolatePaths(path1, path2, divider):
	newPath = GSPath()
	for i in range(len(path1.nodes)):
		node1 = path1.nodes[i]
		node2 = path2.nodes[i]
		
		virtualNode = GSNode()
		virtualNode.position = averageXY (node1, node2, divider)
		virtualNode.connection = path1.nodes[i].connection
		virtualNode.type = path1.nodes[i].type
		
		newPath.nodes.append(virtualNode)
		
	thisGlyph.layers[LAYER].paths.append( newPath )
	return newPath
		
def averageXY (node1, node2, divider):
	XX = node1.x + (node2.x - node1.x) * divider
	YY = node1.y + (node2.y - node1.y) * divider
	return XX, YY


def offset(path):
	print path.nodes
	print "---"

def process(thisGlyph):
	if detectPaths(thisGlyph):
	 	path1 = detectPaths(thisGlyph)[0]
	 	path2 = detectPaths(thisGlyph)[1]

		# Make sure the paths are equal
	 	if len(path1) == len(path2):
	 		for i in range(HOWMANYLINES):
	 			divider = 1 / float(HOWMANYLINES+1)
 				interpolatePaths(path1, path2, divider*(i+1))

	 	else:
	 		print "paths are not equal"
	else:
	 	print "you have to select two paths..."
	 	
Font.disableUpdateInterface()
for thisGlyph in selectedGlyphs:
	process( thisGlyph )
Font.enableUpdateInterface()

# print "I'm done"




