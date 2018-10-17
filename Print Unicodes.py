#MenuTitle: Print Glyph Names and Unicodes
# -*- coding: utf-8 -*-

__doc__="""
Print the glyph name and its unicode
"""

import GlyphsApp

Font = Glyphs.font
selectedGlyphs = [ x.parent for x in Font.selectedLayers ]

def process( thisGlyph ):
	print thisGlyph.name, "|", thisGlyph.unicode

Font.disableUpdateInterface()

for thisGlyph in selectedGlyphs:
	process( thisGlyph )

Font.enableUpdateInterface()
