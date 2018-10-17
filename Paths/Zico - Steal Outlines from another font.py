#MenuTitle: Zico | Steal Outlines from Other Font
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
#		- based on Rainer's Steal Kerning script
#
#	_TODO:
#		- 
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


"""Copy Outlines from one font to another."""

import vanilla
import copy

class GroupsCopy(object):

	def __init__(self):
		self.w = vanilla.FloatingWindow((400, 70), "Text from line 8")
		
		self.w.text_anchor = vanilla.TextBox((15, 12+2, 130, 14), "Copy Outlines from:", sizeStyle='small')
		self.w.from_font = vanilla.PopUpButton((150, 12, 150, 17), self.GetFonts(isSourceFont=True), sizeStyle='small', callback=self.buttonCheck)
		
		self.w.text_value = vanilla.TextBox((15, 12+2+25, 130, 14), "To selected glyphs in:", sizeStyle='small')
		self.w.to_font = vanilla.PopUpButton((150, 12+25, 150, 17), self.GetFonts(isSourceFont=False), sizeStyle='small', callback=self.buttonCheck)

		self.w.copybutton = vanilla.Button((-80, 12+25, -15, 17), "Copy", sizeStyle='small', callback=self.copyOutlines)
		self.w.setDefaultButton( self.w.copybutton )

		self.w.open()
		self.buttonCheck(None)
		
	def GetFonts(self, isSourceFont):
		myFontList = [ "%s - %s" % ( x.font.familyName, x.selectedFontMaster().name ) for x in Glyphs.orderedDocuments() ]

		if isSourceFont:
			myFontList.reverse()
		
		return myFontList
	
	def buttonCheck(self, sender):
		fromFont = self.w.from_font.getItems()[ self.w.from_font.get() ]
		toFont   = self.w.to_font.getItems()[ self.w.to_font.get() ]

		if fromFont == toFont:
			self.w.copybutton.enable( onOff=False )
		else:
			self.w.copybutton.enable( onOff=True )
	
	def copyOutlines(self, sender):
		fromFont = self.w.from_font.getItems()[ self.w.from_font.get() ]
		toFont   = self.w.to_font.getItems()[ self.w.to_font.get() ]
		
		Doc_source      = [ x for x in Glyphs.orderedDocuments() if ("%s - %s" % ( x.font.familyName, x.selectedFontMaster().name )) == fromFont ][0]
		Master_source   = Doc_source.selectedFontMaster().id
		Font_source     = Doc_source.font
		Font_target     = [ x.font for x in Glyphs.orderedDocuments() if ("%s - %s" % ( x.font.familyName, x.selectedFontMaster().name )) == toFont ][0]
		Glyphs_selected = [ x.parent for x in Font_target.parent.selectedLayers() ]
		
		print "Syncing Outlines for", len(Glyphs_selected), "glyphs from", Font_source.familyName, "to", Font_target.familyName, ":"
		

		for thisGlyph in Glyphs_selected:
				glyphName = thisGlyph.name
				sourceGlyph = Font_source.glyphs[ glyphName ]
				
				for layer in range(len(thisGlyph.layers)):

					if (sourceGlyph.layers[layer].paths):
						thisGlyph.layers[layer].paths = copy.copy(sourceGlyph.layers[layer].paths)
						print "   ", glyphName, "paths"

					if (sourceGlyph.layers[layer].components):
						thisGlyph.layers[layer].components = copy.copy(sourceGlyph.layers[layer].components)
						print "   ", glyphName, "comps"

					if (sourceGlyph.layers[layer].anchors):
						thisGlyph.layers[layer].anchors = copy.copy(sourceGlyph.layers[layer].anchors)
						print "   ", glyphName, "anchors"

					thisGlyph.layers[layer].RSB = sourceGlyph.layers[layer].RSB
					
		self.w.close()
		
GroupsCopy()
