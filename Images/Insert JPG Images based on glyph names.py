#MenuTitle: Insert JPG Images according to the glyph names
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
#		- Rainer did it, probably better.
#
#	_TODO:
#		- interface for the Y transformation
#		- unite JPG or PNG
#		- if there's no file - don't try to add image, it results in a missing icon...
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


import GlyphsApp

Font = Glyphs.font
selectedLayers = Font.selectedLayers
selectedMaster = Font.selectedFontMaster

FOLDER = GetFolder(message=None, allowsMultipleSelection = False)

def process( thisLayer ):
	NAME = thisLayer.parent.name
	IMAGE = "%s/" % FOLDER+NAME+".jpg"
	DESC = selectedMaster.descender
	
	#hack
	DESC = -277
	
	thisLayer.backgroundImage = GSBackgroundImage(IMAGE)
	thisLayer.RSB = 0
	
	thisLayer.backgroundImage.position = NSPoint(0, DESC)
	
Font.disableUpdateInterface()

for thisLayer in selectedLayers:
	process( thisLayer )

Font.enableUpdateInterface()
