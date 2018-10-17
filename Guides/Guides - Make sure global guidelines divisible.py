#MenuTitle: Make sure global guidelines divisible by 12
# -*- coding: utf-8 -*-

__doc__="""
Make sure global guidelines divisible by 12
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
#		- After creating the Small Caps glyph - it adds the mother glyph as a component.
#
#	_TODO:
#		- Make a GuideMaker out of it.
#		- choose label to each guide
#		- round nearby guides?
#		- Divisionable by XX as option 
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


import GlyphsApp

Font = Glyphs.font

# ---------------- #


Font.disableUpdateInterface()


for master in Font.masters:
	for guide in master.guides:
# 		# check make sure they are all divided by 12 !!
		if guide.y % 12 != 0:
			print master.name, guide.y, " is not divided by 12"
			guide.name = None
			
		if guide.y == 684:
			guide.name = "ASC"
			
		if guide.y == -240:
			guide.name = "DSC2"		
		
		if guide.y == -204:
			guide.name = "DSC1"		
								
Font.enableUpdateInterface()

print "I'm done"

