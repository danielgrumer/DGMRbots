#MenuTitle: Instances | Create Instances
# -*- coding: utf-8 -*-

# A script that creates instances based on weight/width values

import GlyphsApp

WEIGHTS = [0, 67, 144, 235, 340, 468, 613, 788, 1000]
WIDTHS = [0, 67, 144, 235, 340, 468, 613, 788, 1000]

for weight in WEIGHTS:
	for width in WIDTHS:
# 		print weight, width
		newInstance = GSInstance()
		newInstance.active = True
		newInstance.name = str(weight) + "  " + str(width)
		newInstance.weightValue = weight
		newInstance.widthValue = width
		newInstance.isItalic = False
		newInstance.isBold = False

		Glyphs.font.addInstance_( newInstance )
		newInstance.updateInterpolationValues()