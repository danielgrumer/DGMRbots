#MenuTitle: Generate Black Box stylistic set
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

def drawContent( thisGlyph, newGlyph, layer, SHAPE, PADDING, ySHIFT, SCALE):

	xSHIFT = thisGlyph.layers[layer].LSB  + PADDING + 20	
	RightSideBearing = f.glyphs[SHAPE].layers[0].RSB
	LeftSideBearing = f.glyphs[SHAPE].layers[0].LSB
	
	
	# Add background component
	newGlyph.layers[layer].components.append(GSComponent(SHAPE))
	newGlyph.layers[layer].components[0].applyTransform((1,0,0,1,thisGlyph.layers[layer].LSB + PADDING,0))
	
	# Decompose
	newGlyph.layers[layer].decomposeComponents()
	
	# Move the dots
	for path in newGlyph.layers[layer].paths:
		path.nodes[0].x += thisGlyph.layers[layer].width * SCALE + PADDING - 1
		path.nodes[1].x += thisGlyph.layers[layer].width * SCALE + PADDING - 1
	
	# First Reverse
	for i in range(len(newGlyph.layers[layer].paths)):
		newGlyph.layers[layer].paths[i].reverse()

	# Add letter component
	newGlyph.layers[layer].components.append(GSComponent(thisGlyph))
	
	# transform
	newGlyph.layers[layer].components[0].applyTransform((SCALE,0,0,SCALE,xSHIFT + PADDING / 2 ,ySHIFT))
	
	# Decompose
	newGlyph.layers[layer].decomposeComponents()
	newGlyph.layers[layer].correctPathDirection()
	newGlyph.layers[layer].roundCoordinates()
	
	# Side Bearing
	newGlyph.layers[layer].RSB = RightSideBearing
	newGlyph.layers[layer].LSB = LeftSideBearing
	
		
def process(thisGlyph, EXT, SHAPE, PADDING, ySHIFT, SCALE):
	newGlyph = createNewGlyph(thisGlyph, EXT)
	drawContent( thisGlyph, newGlyph, 0, SHAPE, PADDING, ySHIFT, SCALE)
	
	
Font.disableUpdateInterface()

for thisGlyph in selectedGlyphs:
	# extention, shape-to-take, Negative?, remove overlap?, vertical-shift
 	process(thisGlyph, ".ss01", "comp_box", 100, 65, 0.8)

for feature in f.features:
        if feature.automatic:
               feature.update()

Font.enableUpdateInterface()


# print "I'm done"