#MenuTitle: Kerning Groups | Add -hb to Hebrew Kerning Groups
# -*- coding: utf-8 -*-

import GlyphsApp

__doc__="""
Add -hb to Hebrew Kerning Groups
"""

import GlyphsApp

Font = Glyphs.font
selectedGlyphs = [ x.parent for x in Font.selectedLayers ]

def process( thisGlyph ):
	NAME = thisGlyph.name
	L = thisGlyph.leftKerningGroup
	R = thisGlyph.rightKerningGroup
	if "-hb" in NAME:
		thisGlyph.leftKerningGroup = L + "-hb"
		thisGlyph.rightKerningGroup = R + "-hb"

Font.disableUpdateInterface()

for thisGlyph in selectedGlyphs:
	process( thisGlyph )

Font.enableUpdateInterface()
