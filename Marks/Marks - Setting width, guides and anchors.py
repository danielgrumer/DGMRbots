#MenuTitle: Marks | Set width, guides and anchors
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
#		- made for Hebrew/Arabic/Latin marks drawing.
#
#	_TODO:
#		- interface
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


import GlyphsApp

Font = Glyphs.font
selectedGlyphs = [ x.parent for x in Font.selectedLayers ]

mid = 200

def process( thisGlyph ):
## Disable Auto Alignment
# 	for i in thisGlyph.layers[1].components:
# 		i.automaticAlignment = False
# 		print i.automaticAlignment

	for l in range(2):
		# Set Width to 400
		thisGlyph.layers[l].width = 400
		
		# Set Anchors
		for i in thisGlyph.layers[l].anchors:
			if i.name == "_top":
				i.y = Font.masters[l].xHeight	
				i.x = mid
			if i.name == "top":
	# 			i.y = 650
				i.x = mid
	
			if i.name == "_bottom":
				i.y = 0	
				i.x = mid
				
			if i.name == "bottom":
	# 			i.y = -250
				i.x = mid

		# Delete guides
		for i in range(len(thisGlyph.layers[l].guides)):	
			del(thisGlyph.layers[l].guides[0])

		# add guidelines
		for i in range(17):
			newGuide = GSGuideLine()
			newGuide.position = NSPoint(0, (i+1) * -20)
			newGuide.angle = 0.0
			thisGlyph.layers[l].guides.append(newGuide)
	
		for i in range(17):
			newGuide = GSGuideLine()
			newGuide.position = NSPoint(0, Font.masters[l].xHeight + (i+1) * 20)
			newGuide.angle = 0.0
			thisGlyph.layers[l].guides.append(newGuide)

Font.disableUpdateInterface()
for thisGlyph in selectedGlyphs:
	process( thisGlyph )
Font.enableUpdateInterface()

print "I'm done"