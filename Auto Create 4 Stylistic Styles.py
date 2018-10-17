#MenuTitle: Abraham | Generate 4 stylistuc sets
# -*- coding: utf-8 -*-

# Auto Create Stylistic Styles

import GlyphsApp

f = Glyphs.font
selectedGlyphs = [ x.parent for x in f.selectedLayers ]

WIDTH = 800
SCALE = 0.7

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

def drawContent( thisGlyph, newGlyph, layer, SHAPE, NEGATIVE, OVERLAP, vSHIFT):
	# Add component
	newGlyph.layers[layer].components.append(GSComponent(thisGlyph))
	
	# transform
	newGlyph.layers[layer].components[0].transform = ((SCALE, 0, 0, SCALE, 0, 0))
	
	# decompose
	newGlyph.layers[layer].decomposeComponents()
	
	# remove overlap
	if OVERLAP:
		newGlyph.layers[layer].removeOverlap()
	
	# Reverse if needed
	if NEGATIVE:
		for i in range(len(newGlyph.layers[layer].paths)):
			newGlyph.layers[layer].paths[i].reverse()

	# adjust side bearings proportionally
# 	ratio = thisGlyph.layers[layer].LSB / thisGlyph.layers[layer].RSB
	bounds = newGlyph.layers[layer].bounds.size.width
	auto = (WIDTH - bounds)/2
	newGlyph.layers[layer].LSB = auto
	
	for i in range(len(newGlyph.layers[layer].paths)):
		newGlyph.layers[layer].paths[i].applyTransform((1,0,0,1,0,vSHIFT))
	
	# set width
	newGlyph.layers[layer].width = WIDTH
	newGlyph.layers[layer].components.append(GSComponent(SHAPE))
		
def process(thisGlyph, EXT, SHAPE, NEGATIVE, OVERLAP, vSHIFT):
	newGlyph = createNewGlyph(thisGlyph, EXT)
	drawContent( thisGlyph, newGlyph, 0, SHAPE, NEGATIVE, OVERLAP, vSHIFT)
	drawContent( thisGlyph, newGlyph, 1, SHAPE, NEGATIVE, OVERLAP, vSHIFT)	
	
	
	
Font.disableUpdateInterface()

for thisGlyph in selectedGlyphs:
	# extention, shape-to-take, Negative?, remove overlap?, vertical-shift
	process(thisGlyph, ".ss01", "c_symbols_circleB", True, True, 60)
 	process(thisGlyph, ".ss02", "c_symbols_circleW", True, True, 60)
 	process(thisGlyph, ".ss03", "c_symbols_squareB", True, True, 60)
 	process(thisGlyph, ".ss04", "c_symbols_squareW", True, True, 60)


for feature in f.features:
        if feature.automatic:
                feature.update()

Font.enableUpdateInterface()


# print "I'm done"