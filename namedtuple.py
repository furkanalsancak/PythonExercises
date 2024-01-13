from collections import namedtuple

#list / tuple
# color = (55,155,255)

#dictionary
#color = {'red': 55, 'green': 155, 'blue': 255}

#namedtuple
Color = namedtuple('Color', ['red', 'green', 'blue'])
color = Color(55,155,255)
white = Color(255,255,255)

print(color[0])
print(color.red)
print(color)
print(white.blue)