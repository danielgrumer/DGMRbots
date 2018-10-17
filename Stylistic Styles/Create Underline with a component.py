#MenuTitle: Create Underline with 'underline' comp
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
#		- made for Inga's project
#
#	_TODO:
#		- don't rely on a component, just draw a path
#		- interface: set the thickness, and offset.
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import GlyphsApp

f = Glyphs.font
selectedGlyphs = [ x.parent for x in f.selectedLayers ]

EXT = '.ss12'
compName = 'underline'

def process(thisGlyph):
		newGlyphName = thisGlyph.name + EXT
		
		# If it exists, clear it
		if f.glyphs[newGlyphName]:
			del(f.glyphs[newGlyphName])
		
		newGlyph = thisGlyph.copy()
		newGlyph.name = newGlyphName
		f.glyphs.append(newGlyph)
		newGlyph.color = 10
		
		# get its width
		w = f.glyphs[newGlyphName].layers[0].width
		
		# place the underline component and decompose
		f.glyphs[newGlyphName].layers[0].components.append(GSComponent(compName))
		f.glyphs[newGlyphName].layers[0].components[-1].decompose()
		
		f.glyphs[newGlyphName].layers[0].paths[-1].nodes[0].x = w
		f.glyphs[newGlyphName].layers[0].paths[-1].nodes[1].x = w


Font.disableUpdateInterface()

for thisGlyph in selectedGlyphs:
	process(thisGlyph)

Font.enableUpdateInterface()

