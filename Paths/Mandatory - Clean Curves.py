#MenuTitle: Mandatory | Remove all BCP Points
# -*- coding: utf-8 -*-
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


# Set anchors positions 
# 
# import GlyphsApp
# 
# Font = Glyphs.font
# selectedGlyphs = [ x.parent for x in Font.selectedLayers ]
# 
# TEST = [0]
# VALUES = [9999, 9999, 9999, 640, 9999, 9999, 9999 ]
# BASELINE = [-9999, -9999, -9999, 31, -9999, -9999, -9999 ]
# 
# def clearOffCurves( thisGlyph ):
# 	for layer in range(len(TEST)):		
# 		for path in thisGlyph.layers[layer].paths:
# 			virtualPath = GSPath()
# 			for node in path.nodes:
# 				if node.type == "offcurve":
# 					print "passed", node
# 				else:
# 					virtualPath.nodes.append(node)
# 			print virtualPath
# 			virtualPath.closed = True
# 			
# 			thisGlyph.layers[layer].removePath_( path )
# 			thisGlyph.layers[layer].paths.append( virtualPath )
# 
# 					
# 									
# def adjust( thisGlyph ):
# 	for layer in range(len(thisGlyph.layers)):		
# 		for path in thisGlyph.layers[layer].paths:
# 			for node in path.nodes:
# 				if node.y > VALUES[layer]:
# 					node.y = 666
# 				if node.y < BASELINE[layer]:
# 					node.y = 0
# 					
# 
# 
# Font.disableUpdateInterface()
# for thisGlyph in selectedGlyphs:
# 	clearOffCurves( thisGlyph )
# 	adjust( thisGlyph )
# Font.enableUpdateInterface()
# 
# print "I'm done"
