#MenuTitle: Make sure global guidelines divisible by 12
# -*- coding: utf-8 -*-

__doc__="""
Make sure global guidelines divisible by 12
"""

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

