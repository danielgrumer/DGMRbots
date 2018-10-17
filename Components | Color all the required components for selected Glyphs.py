NOT FINISHED!!!

#MenuTitle: Copy-Pasting  | Color all the components that are contained by selected Glyphs
# -*- coding: utf-8 -*-
__doc__="""
Color all the components that are contained by selected Glyphs
"""

Font = Glyphs.font
selectedGlyphs = [ x.parent for x in Font.selectedLayers ]

# ---------------- #

def color(WHO, COLOR):
	for g in WHO:
		g.color = COLOR

ALLCOMPS = []

def checkWhichComps(WHO):
	NEEDEDCOMPS = []
	for g in WHO:		
		for l in g.layers:	
			for comp in l.components:
				if comp.componentName not in NEEDEDCOMPS:
					NEEDEDCOMPS.append(comp.componentName)
			for h in l.hints:
				if h.type == CORNER:
					NEEDEDCOMPS.append(h.name)					
	return NEEDEDCOMPS
		

def process(WHO):
	print checkWhichComps(WHO)

Font.disableUpdateInterface()

# remove all colors, and only mark the wanted glyphs
color(Font.glyphs, 9223372036854775807)
color(selectedGlyphs, 1)

process(selectedGlyphs)
	
Font.enableUpdateInterface()
	