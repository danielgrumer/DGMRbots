#MenuTitle: Glyph Shaker
# -*- coding: utf-8 -*-

__doc__="""
Goes through all selected glyphs and slaps each of their nodes around a bit.
"""

import GlyphsApp

#Font = Glyphs.font
#selectedGlyphs = [ x.parent for x in Font.selectedLayers ]

XVALUE = 14 
YVALUE = 8


import random
random.seed()

selectedLayers = Glyphs.font.selectedLayers

for thisLayer in selectedLayers:
    for thisPath in thisLayer.paths:
        for thisNode in thisPath.nodes:
            thisNode.x += random.randint( -XVALUE, XVALUE )
            thisNode.y += random.randint( -YVALUE, YVALUE )
            
#print "I'm done"