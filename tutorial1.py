from ggame import App

from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

# Three primary colors with no transparency (alpha = 1.0)
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
yellow = Color(0x999900, 1.0)

# Define a line style that is a thin (1 pixel) wide black line
thinline = LineStyle(1, black)
# A graphics asset that represents a rectangle

#Main square of the house
house = RectangleAsset(300, 300, thinline, blue)

#Roof
roof = PolygonAsset ([(0, 100), (200, 0), (400, 100), (0, 100)], thinline, red)

#sun
sun = EllipseAsset (70, 70, thinline, yellow)


#ellipse = EllipseAsset (50, 20, thinline, blue)
#hexagon = PolygonAsset ([(0, 0), (200, 0), (250, 250), (0, 0)], thinline, red)

#Sprites
Sprite(house, (250, 250))
Sprite(roof, (200, 150))
Sprite(sun)

myapp = App()
myapp.run()