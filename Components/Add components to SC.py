#MenuTitle: Adds the right component to a smallcap glyph
# -*- coding: utf-8 -*-

import GlyphsApp

Font = Glyphs.font
selectedGlyphs = [ x.parent for x in Font.selectedLayers ]

def process( thisGlyph ):
	name, ext = thisGlyph.name.split(".")
	thisGlyph.layers[0].components.append(GSComponent(name))
	thisGlyph.layers[1].components.append(GSComponent(name))
	
Font.disableUpdateInterface()

for thisGlyph in selectedGlyphs:
	process( thisGlyph )

Font.enableUpdateInterface()