#MenuTitle: Mandatory | Remove all BCP Points
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
#		- leave only straight lines. 
#
#	_TODO:
#		- make it work on several layers at a time
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



__doc__="""
Delete all the curves! used for Mandatory
"""

import GlyphsApp

Font = Glyphs.font
selectedGlyphs = [ x.parent for x in Font.selectedLayers ]


def clearOffCurve( thisGlyph ):
	for l in range(len(thisGlyph.layers)):
		thisLayer = thisGlyph.layers[l]
		
		virtualPaths = []
		
		for thisPath in thisLayer.paths:
			# go through all paths and deposit copies of them in vitualPaths
			
			currentNodes = thisPath.nodes
			virtualPath = GSPath()
			
			for i in range( len( currentNodes )):
				thisNode = currentNodes[ i ]
				try:
					previousNode = currentNodes[ i-1 ]
				except:
					previousNode = currentNodes[ -1 ]
				if thisNode.type != "offcurve":
					# copy the node:
					virtualNode = GSNode()
					virtualNode.position = thisNode.position
					virtualNode.connection = thisNode.connection
					virtualNode.type = "line"
					virtualPath.nodes.append( virtualNode )
				virtualPath.closed = True
			virtualPaths.append( virtualPath )
		
		# delete the original paths:
		for i in range( len( thisLayer.paths ) )[::-1]:
			thisLayer.removePath_( thisLayer.paths[i] )
		
		# add the virtual paths:
		for thisVirtualPath in virtualPaths:
			thisLayer.paths.append( thisVirtualPath )
		

Font.disableUpdateInterface()

for thisGlyph in selectedGlyphs:
	print "Processing", thisGlyph.name
	thisGlyph.beginUndo()
	clearOffCurve( thisGlyph )
	thisGlyph.endUndo()

Font.enableUpdateInterface()
