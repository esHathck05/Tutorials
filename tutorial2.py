from ggame import App, Color, LineStyle, Sprite
from ggame import CircleAsset

red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)

thinline = LineStyle(1, black)
mycircle = CircleAsset(5, thinline, blue)
mycircle2 = CircleAsset(2,thinline, red)
xcoordinates = range(100, 600, 10)
ycoordinates = range(50, 550, 5)

# Generate a list of sprites that form a line!
sprites = [Sprite(mycircle, (x, x*0.5 + 100)) for x in xcoordinates]
sprites = [Sprite(mycircle2, (x+200, x)) for x in ycoordinates]


myapp = App()
myapp.run()
