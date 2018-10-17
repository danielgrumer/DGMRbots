#MenuTitle: Zico Display | Match all Display styles
# -*- coding: utf-8 -*-

# A script that checks the consistency in ZicoDisplay


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#	Version: 0.1
#
#	>> Daniel Grumer
#	>> www.danielgrumer.com <<
#
#	_NOTES:
#		- Was made before purchasing Yanone's SpaceBar.
#
#	_TODO:
#		- The only reason to work on it is to generate a XLS, that will color the inconsistencies
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


import GlyphsApp
import copy
from pprint import pprint
import csv

Font = Glyphs.font

HebrewLetters = [
	"alef-hb",
	"bet-hb",
	"gimel-hb",
	"dalet-hb",
	"he-hb",
	"vav-hb",
	"zayin-hb",
	"het-hb",
	"tet-hb",
	"yod-hb",
	"kaf-hb",
	"finalkaf-hb",
	"lamed-hb",
	"mem-hb",
	"finalmem-hb",
	"nun-hb",
	"finalnun-hb",
	"samekh-hb",
	"ayin-hb",
	"pe-hb",
	"finalpe-hb",
	"tsadi-hb",
	"finaltsadi-hb",
	"qof-hb",
	"resh-hb",
	"shin-hb",
	"tav-hb",
]

labels = ["Thin", "Thin Inline", "Black", "Black Inline"]
def collect():
	collection = []
	for letter in HebrewLetters:
		data = {}
		data["name"] = letter
		for i in range(4):
			char = Glyphs.font.glyphs[letter].layers[i]
			data[labels[i]] = char.width - char.RSB - char.LSB
		collection.append(data)
	return collection
			
Font.disableUpdateInterface()
print collect()
Font.enableUpdateInterface()

# print "I'm done"


