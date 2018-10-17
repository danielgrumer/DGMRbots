#MenuTitle: Components | Find out in which Glyphs a comp exists
# -*- coding: utf-8 -*-
__doc__="""
Find out in which Glyphs a comp exists
"""

Font = Glyphs.font
selectedGlyphs = [ x.parent for x in Font.selectedLayers ]

# ---------------- #

#Which comp are you looking for?
FIND = "c_ar_bath_noonEnd.001"

def findComp(thisGlyph):
	for comp in thisGlyph.layers[1].components:
		if (comp.componentName == FIND):
			print thisGlyph.name

Font.disableUpdateInterface()		
for thisGlyph in selectedGlyphs:
	#print "Processing", thisGlyph.name
	findComp(thisGlyph)

Font.enableUpdateInterface()
print "I'm done"
	