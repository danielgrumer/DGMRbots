import GlyphsApp

Font = Glyphs.font
selectedGlyphs = [ x.parent for x in Font.selectedLayers ]

path = u"/Users/Daniel/Dropbox/ArLaHe/Arabic Basic.txt"

paths = [
    u"/Users/Daniel/Dropbox/ArLaHe/CharacterSet/Arabic Basic.txt",
    u"/Users/Daniel/Dropbox/ArLaHe/CharacterSet/Arabic Components.txt",
    u"/Users/Daniel/Dropbox/ArLaHe/CharacterSet/Hebrew Marks and Punctuation.txt",
    u"/Users/Daniel/Dropbox/ArLaHe/CharacterSet/Hebrew Basic.txt"
]  

lines = []

for path in paths:
    txt = open(path, 'r')
    fileLines = txt.read()
    txt.close()
    fileLines = fileLines.split("\n")
    lines += fileLines

cmap = {}
for l in lines:
    name, uniString = l.split(" | ")
    if uniString == "None":
        cmap[name] = None
    else:
        uniValue = int("0x"+uniString, 16)
        cmap[name] = uniValue
        
def process( thisGlyph ):
	if thisGlyph.name in cmap:
		if thisGlyph.unicode is None:
			print thisGlyph.name
			oldUni = thisGlyph.unicode
			newUni = cmap[thisGlyph.name]
			thisGlyph.unicode = hex(newUni)
			print "--"

Font.disableUpdateInterface()

for thisGlyph in selectedGlyphs:
	process( thisGlyph )

Font.enableUpdateInterface()