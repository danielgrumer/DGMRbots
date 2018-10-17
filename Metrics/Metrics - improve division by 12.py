#MenuTitle: Improve the division by 12
# -*- coding: utf-8 -*-

__doc__="""
Improve the division by 12
"""

import GlyphsApp

Font = Glyphs.font
selectedGlyphs = [ x.parent for x in Font.selectedLayers ]

MN = 12

def process( thisGlyph ):
 	for l in range(len(thisGlyph.layers)):
 		L = thisGlyph.layers[l].LSB
 		rest = L % MN
 		
 		# if that's not zero...
 		if (rest > 0):
 			# if that's 1/2/3/4/5...
 			if (rest < 6):
 				thisGlyph.layers[l].LSB -= rest
 				print "changed" + thisGlyph.name, thisGlyph.layers[l].LSB
 			
 			#if that's 7/8/9/10/11...	
 			if (rest > 6):
 				thisGlyph.layers[l].LSB += (MN - rest)
 				print "changed " + thisGlyph.name, thisGlyph.layers[l].LSB

			# if that's a number is 6	
 			else: 
 				thisGlyph.layers[l].LSB -= 6
 				print thisGlyph.name + " was 6"
 		
 		
Font.disableUpdateInterface()
for thisGlyph in selectedGlyphs:
	process( thisGlyph )
Font.enableUpdateInterface()

print "I'm done"