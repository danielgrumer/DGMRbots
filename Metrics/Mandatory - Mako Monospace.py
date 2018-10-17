#MenuTitle: Find average width
# -*- coding: utf-8 -*-

__doc__="""
Find average width
"""

Font = Glyphs.font
selectedGlyphs = [ x.parent for x in Font.selectedLayers ]

# ---------------- #

DUO = True
TRIO = True

def makeMonospace(WHO, WIDTHS):
	# each glyph
	for g in WHO:
		#  each layer
		for i in range(len(g.layers)):
			thisLayer = g.layers[i]
			thisLayer.decomposeCorners()	
			thisLayer.decomposeComponents()
			thisLayer.correctPathDirection()
			
			NET = thisLayer.width - (thisLayer.RSB + thisLayer.LSB)
			BRUT = WIDTHS[i]
			
			
			if TRIO:
				if (NET > BRUT*1.2):
					BRUT = WIDTHS[i]*1.5
			
			if DUO:		
				if (NET+NET < BRUT):
					BRUT = WIDTHS[i]/2
			
			SB = BRUT - NET
				
			thisLayer.LSB = SB/2
			thisLayer.RSB = SB/2
			
			thisLayer.width = BRUT
	

def findAverageWidth(WHO):
	WIDTHS = []
	for i in range(4):
		W = []
		for g in WHO:
			W.append(g.layers[i].width)
		WIDTHS.append(int(round(reduce(lambda x, y: x + y, W) / len(W))))
	
	return WIDTHS
			

Font.disableUpdateInterface()

WIDTHS = [320, 560, 320, 560]
makeMonospace(selectedGlyphs, WIDTHS)

Font.enableUpdateInterface()
	