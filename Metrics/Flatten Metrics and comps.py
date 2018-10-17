#MenuTitle: Flatten Metrics and comps
# -*- coding: utf-8 -*-

__doc__="""
Flatten metrics and comps
"""

Font = Glyphs.font
selectedGlyphs = [ x.parent for x in Font.selectedLayers ]

# ---------------- #

def flattenMetrics(WHO):
	for g in WHO:
		for i in range(len(g.layers)):
			
			# if there are components
			if g.layers[i].components:
				for comp in g.layers[i].components:
					comp.setDisableAlignment_( True )

				g.layers[i].decomposeCorners()	
				g.layers[i].decomposeComponents()
				g.layers[i].removeOverlap()
				g.layers[i].correctPathDirection()
			
# 			g.layers[i].setRightMetricsKey_(None)
# 			g.layers[i].setLeftMetricsKey_(None)
			
				g.layers[i].leftMetricsKey = None
			
				L = int(g.layers[i].LSB)
				R = int(g.layers[i].RSB)
	
				g.layers[i].LSB = L
				g.layers[i].RSB = R

Font.disableUpdateInterface()

flattenMetrics(selectedGlyphs)	

Font.enableUpdateInterface()
	