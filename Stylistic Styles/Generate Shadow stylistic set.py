#MenuTitle: Generate Shadow stylistic set
# -*- coding: utf-8 -*-

import GlyphsApp

f = Glyphs.font
selectedGlyphs = [ x.parent for x in f.selectedLayers ]

def createNewGlyph( thisGlyph, EXT ):
	# Get the name
	name = thisGlyph.name
	if "." in name:
		name = name.split(".")[0]
	name += EXT
	
	# If it exists, clear it
	if f.glyphs[name]:
		del(f.glyphs[name])

	# Create new Glyph name and label it
	f.glyphs.append(GSGlyph(name))
	newGlyph = f.glyphs[name]
	newGlyph.color = 8
	return newGlyph

def drawContent( thisGlyph, newGlyph, layer, SHAPE):

	RightSideBearing = f.glyphs[SHAPE].layers[0].RSB
	LeftSideBearing = f.glyphs[SHAPE].layers[0].LSB
	
	
	# Add background component
	newGlyph.layers[layer].components.append(GSComponent(SHAPE))
	
	# Decompose
	newGlyph.layers[layer].decomposeComponents()
	
	# Move the dots
	for path in newGlyph.layers[layer].paths:
		path.nodes[0].x += thisGlyph.layers[layer].width - thisGlyph.layers[layer].RSB - 1 
		path.nodes[1].x += thisGlyph.layers[layer].width - thisGlyph.layers[layer].RSB - 1 
 		path.nodes[2].x += thisGlyph.layers[layer].LSB
 		path.nodes[3].x += thisGlyph.layers[layer].LSB
		

	# Add letter component
	newGlyph.layers[layer].components.append(GSComponent(thisGlyph))
		
	# Decompose
	newGlyph.layers[layer].decomposeComponents()
	newGlyph.layers[layer].correctPathDirection()
	newGlyph.layers[layer].roundCoordinates()
	
	# Side Bearing
	newGlyph.layers[layer].RSB = thisGlyph.layers[layer].RSB
# 	newGlyph.layers[layer].LSB = LeftSideBearing
	
		
def process(thisGlyph, EXT, SHAPE):
	newGlyph = createNewGlyph(thisGlyph, EXT)
	drawContent( thisGlyph, newGlyph, 0, SHAPE)
	
	
Font.disableUpdateInterface()

for thisGlyph in selectedGlyphs:
	# extention, shape-to-take, Negative?, remove overlap?, vertical-shift
 	process(thisGlyph, ".ss07", "comp_shadow1")

for feature in f.features:
        if feature.automatic:
               feature.update()

Font.enableUpdateInterface()


# print "I'm done"