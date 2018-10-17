#MenuTitle: Sort Glyphs by Width

# -*- coding: utf-8 -*-
__doc__="""
Sort Glyphs by Width
"""

Font = Glyphs.font
selectedGlyphs = [ x.parent for x in Font.selectedLayers ]

# ---------------- #


def collectWidths(WHO):
	WIDTHS = []

	# collect all the widths
	for g in WHO:
 		WIDTHS.append((str(g.name),g.layers[0].width))

	# sort it
	WIDTHS = sorted(WIDTHS, key=lambda x: x[1])

	# extract the names only
	WIDTHS = [x[0] for x in reversed(WIDTHS)]
	
	return WIDTHS

Font.disableUpdateInterface()

print collectWidths(selectedGlyphs)	

Font.enableUpdateInterface()
	