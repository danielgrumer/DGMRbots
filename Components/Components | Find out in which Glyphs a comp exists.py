#MenuTitle: Components | Find out in which Glyphs a comp exists
# -*- coding: utf-8 -*-
__doc__="""
Find out in which Glyphs a comp exists
"""

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#	Version: 0.1
#
#	>> Daniel Grumer
#	>> www.danielgrumer.com <<
#
#	_NOTES:
#		- made for an Arabic project, good for checking if 
#
#	_TODO:
#		- Maybe it can be replaced with a script called "Remove Unused Components"
#		- interface
#		- multi layer support
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


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
	findComp(thisGlyph)

Font.enableUpdateInterface()
print "I'm done"
	