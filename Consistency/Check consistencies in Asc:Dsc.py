#MenuTitle: Abraham | Check consistencies in Asc/Dsc angles
# -*- coding: utf-8 -*-

# Check consistencies in Asc/Dsc angles

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#	Version: 0.1
#
#	>> Daniel Grumer
#	>> www.danielgrumer.com <<
#
#	_NOTES:
#		- Part of the Abraham QA
#
#	_TODO:
#		- Make it work on any numer of layers
#		- Maybe it can identify the asc + dsc automatically?
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


import GlyphsApp
import math
import pprint

f = Glyphs.font

Ascenders = ["b", "d", "k", "l", "t", "c_la_stemAscLC"]
Descenders = ["f.salt", "g", "g.salt", "p", "q", "y"]

ArabicAscenders = [
	"c_ar_tahPole",
	"alef_ar",
	"kaf_ar",
	"lam_ar",
	"dotlessbeh_ar",
	"alef_short_ar",
	"alef_ar.fina",
	"dal_ar.fina",
	"reh_ar.fina",
	"seen_ar.fina",
	"lam_alef_ar.fina",
	"alef_short_ar.fina",
	"dotlessbeh_ar.init",
	"lam_ar.medi",
	"c_lam_alef_short_ar.fina",
	]

layer = 1    # 0 for light, 1 for bold
 
def process(myList, layer, REVERSE):
	summary = []	
	for g in f.glyphs:
		values = []	
		if g.name in myList:
			for i in range(len(g.layers[layer].paths)):
				for j in range(len(g.layers[layer].paths[i])):
					values.append((g.layers[layer].paths[i].nodes[j].x, g.layers[layer].paths[i].nodes[j].y))
			values = sorted(values, key=lambda x: x[1])	
			if REVERSE:
				values.reverse()
			x1,y1 = values[-1]
			x2,y2 = values[-2]
			
			dx = abs( x1 - x2)
			dy = abs( y1 - y2)
			
			dist = math.sqrt( (x2 - x1)**2 + (y2 - y1)**2 )
				
			data = int(round(dist)), "{%s x %s}" % (int(dx), int(dy)), str(g.name)
			summary.append(data)
	summary = sorted(summary, key=lambda x: x[0])
	pprint.pprint(summary)
			
Font.disableUpdateInterface()

print "----- Latin Ascenders -----"
print "-Light-"
process(Ascenders, 0, False)
print "-Bold-"
process(Ascenders, 1, False)

print "----- Latin ArabicAscenders -----"
print "-Light-"
process(ArabicAscenders, 0, False)
print "-Bold-"
process(ArabicAscenders, 1, False)


print "----- Descenders -----"
print "-Light-"
process(Descenders, 0, True)
print "-Bold-"
process(Descenders, 1, True)

Font.enableUpdateInterface()

print "------- I'm done --------"
