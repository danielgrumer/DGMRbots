#MenuTitle: Insert PNG Images according to the glyph names
# -*- coding: utf-8 -*-

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#	Version: 0.2
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
	IMAGE = "%s/" % FOLDER+NAME+".png"
	DESC = selectedMaster.descender
	
	#hack
	DESC = -250
	
	thisLayer.backgroundImage = GSBackgroundImage(IMAGE)
	
	thisLayer.backgroundImage.transform = ((
        1.0, # x scale factor
        0.0, # x skew factor
        0.0, # y skew factor
        1.0, # y scale factor
        0.0, # x position
        DESC  # y position
        ))
		
Font.disableUpdateInterface()

for thisLayer in selectedLayers:
	process( thisLayer )

Font.enableUpdateInterface()
