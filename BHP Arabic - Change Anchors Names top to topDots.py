#MenuTitle: BHP Arabic | Change Anchors Names from top to topDots and bottom to bottomDotss
# -*- coding: utf-8 -*-
__doc__="""
Change Anchors Names from top to topDots and bottom to bottomDots
"""

import math

Font = Glyphs.font
selectedGlyphs = [ x.parent for x in Font.selectedLayers ]

# ---------------- #

def addNewAnchor(ANCHORNAME, myX, myY):
	newAnchor = GSAnchor()
	newAnchor.name = ANCHORNAME
	newAnchor.position = NSPoint(myX, myY)
	thisGlyph.layers[1].addAnchor_( newAnchor )
	print "added" + ANCHORNAME
	
def nudgeAnchor(i, myX, myY):
	i.x += myX
	i.y += myY

def changeNames(thisGlyph):
	for i in thisGlyph.layers[1].anchors:
		if (i.name == '_top'):
			i.name = '_topDots'
		
		elif (i.name == 'top'):
			i.name = 'topDots'
		
		elif (i.name == '_bottom'):
			i.name = '_bottomDots'
		
		elif (i.name == 'bottom'):
			i.name = 'bottomDots'

		elif (i.name == '_top_2'):
			i.name = '_topDots2'
		
		elif (i.name == 'top_2'):
			i.name = 'topDots2'
		
		elif (i.name == '_bottom_2'):
			i.name = '_bottomDots2'
		
		elif (i.name == 'bottom_2'):
			i.name = 'bottomDots2'


Font.disableUpdateInterface()		
for thisGlyph in selectedGlyphs:
	print "Processing", thisGlyph.name
	changeNames(thisGlyph)

Font.enableUpdateInterface()
print "I'm done"
	