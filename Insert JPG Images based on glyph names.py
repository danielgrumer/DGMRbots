#MenuTitle: Insert JPG Images according to the glyph names
# -*- coding: utf-8 -*-

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
