#MenuTitle: Smooth node to horizontal segment
# -*- coding: utf-8 -*-

__doc__="""
Smooth node to horizontal segment
"""

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#	Version: 0.2
#
#	>> Daniel Grumer
#	>> www.danielgrumer.com <<
#
#	_NOTES:
#		- A horizontal version of the legendary vertical script... made for Kajag
#
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import GlyphsApp

Font = Glyphs.font
selectedGlyphs = [ x.parent for x in Font.selectedLayers ]

def process( thisGlyph ):
	thisLayer = Font.selectedLayers[0]
	DELTA = 20
	selectedPaths = []
	unselectedPaths = []

	# find out which paths has the selected nodes in it, and which don't
	for i, p in enumerate(thisLayer.paths):
		unselectedPaths.append(p)
		for n in p.nodes:
			if n.selected == True:
				if p not in selectedPaths:
					selectedPaths.append(p)
				if p in unselectedPaths:
					unselectedPaths.remove(p)
	
	# go over each path that has nodes in it
	for oldPath in selectedPaths:
		newPath = oldPath.copy()
		selectedNodes = []
	
		# go over nodes, check who's selected + index
		for i, n in enumerate(oldPath.nodes):
			if n.selected == True:
				selectedNodes.append((n.x, n.y, i))
		
		# go over all selected nodes, and make the split
		for i, thisNode in enumerate(selectedNodes):
			newNode = GSNode()
			newNode.smooth = True
			newNode.x = thisNode[0]
			newNode.y = thisNode[1]
			oldIndex = thisNode[2]
			dotsAddedToThisPath = i			
		
  			# Adjust the X values
  			otherNode = newPath.nodes[oldIndex+i]
			if (oldPath.nodes[oldIndex-1].x > newNode.x):
				otherNode.x += DELTA/2
				newNode.x -= DELTA/2
			else:
				otherNode.x -= DELTA/2
				newNode.x += DELTA/2
				
  			# add the dot!
			newPath.insertNode_atIndex_(newNode, oldIndex+1+dotsAddedToThisPath)
 		
 		# draw the path!
		thisLayer.removePath_(oldPath)
		thisLayer.addPath_(newPath)
		thisLayer.correctPathDirection()

Font.disableUpdateInterface()

for thisGlyph in selectedGlyphs:
	process( thisGlyph )

Font.enableUpdateInterface()

