import math
import matplotlib.pyplot as plt

chars = [
[
    "  mmm ",
    " m   m ",
    " m   m ",
    " mmmmm",
    " m   m",
    " m   m",
    " m   m",
],
[
    "mmmm",
    "m   m",
    "m   m",
    "mmmm",
    "m   mm",
    "m    m",
    "mmmmm",
],
[
    "  mmm",
    " m   m",
    "m     ",
    "m     ",
    "m     ",
    " m   m",
    "  mmm ",
    
],[
    "mmmm",
    "m   m",
    "m    m",
    "m    m",
    "m    m",
    "m   m",
    "mmmm",
    
],[
    "mmmmmm",
    "m     ",
    "m     ",
    "mmmmm",
    "m     ",
    "m     ",
    "mmmmmm",
    
],[
    "mmmmmm",
    "m",
    "m ",
    "mmmmm ",
    "m",
    "m",
    "m",
    
],[
    "  mmm",
    " m   m",
    "m     ",
    "m  mmmm",
    "m    m",
    " m   m",
    "  mmm ",
    
],[
    "m    m",
    "m    m",
    "m    m",
    "mmmmmm",
    "m    m",
    "m    m",
    "m    m",
    
],[
    " mmmmm",
    "   m",
    "   m     ",
    "   m     ",
    "   m     ",
    "   m",
    " mmmmm",
    
],[
    "mmmmmm",
    "   m",
    "   m     ",
    "   m     ",
    "   m     ",
    "m  m",
    " mm",
],[
    "m   m",
    "m  m",
    "m m",
    "mm",
    "m m",
    "m  m",
    "m   m",
    
],[
    "m",
    "m",
    "m",
    "m",
    "m",
    "m",
    "mmmmm",
    
],[
    "m     m",
    "mm   mm",
    "mm   mm",
    "m m m m",
    "m mmm m",
    "m  m  m ",
    "m  m  m",
    
],[
    "m    m",
    "mm   m",
    "m m  m",
    "m  m m",
    "m   mm",
    "m    m",
    "m    m",
    
],[
    "  mmm",
    " m   m",
    "m     m",
    "m     m",
    "m     m",
    " m   m",
    "  mmm ",
    
],[
    " mmmm",
    " m   m",
    " m   m",
    " mmmm",
    " m",
    " m",
    " m ",
],[
    "  mmm",
    " m   m",
    "m     m",
    "m     m",
    "m   m m",
    " m   m",
    "  mmm m",
],[
    "mmmm",
    "m   m",
    "m   m",
    "mmmm",
    "m m",
    "m  m",
    "m   m",
], [
    " mmmmm ",
    "m     m",
    "m     ",
    " mmmmm   ",
    "      m",
    "m     m",
    " mmmmm ",
], [
    " mmmmm ",
    "   m",
    "   m",
    "   m",
    "   m",
    "   m",
    "   m",
], [
    " m   m ",
    " m   m ",
    " m   m ",
    " m   m ",
    " m   m ",
    " m   m",
    "  mmm",
], [
    " m   m ",
    " m   m ",
    " m   m ",
    " m   m ",
    "  m m ",
    "  m m",
    "   m",
], [
    "m  m  m ",
    "m  m  m ",
    "m  m  m ",
    "m  m  m ",
    " m m m ",
    " mm mm",
    "  m m",
], [
    " m   m ",
    " m   m ",
    "  m m ",
    "   m ",
    "  m m ",
    " m   m ",
    " m   m",
], [
    " m   m ",
    " m   m ",
    "  m m ",
    "   m ",
    "   m  ",
    "   m",
    "   m",
],  [
    " mmmmm",
    "     m",
    "    m ",
    "   m ",
    "  m   ",
    " m    ",
    " mmmmm",
]
]

MAGNITUDE_SCALE = 1000

RAD_TO_DEG = 180 / math.pi
SPACING = 8
CHARS_PER_ROW = 6

x_shift = -16
y_shift = -16

Xs = []
Ys = []
thetas = []
magnitudes = []

def rect_to_polar(rect):
    x = rect[0]
    y = rect[1]
    theta = math.atan2(y, x)
    mag = math.sqrt(math.pow(x, 2) + math.pow(y, 2))/1000
    return (theta, mag)

def polar_to_rect(polar):
    theta = polar[0]
    mag = polar[1]
    x = mag*math.cos(theta)
    y = mag*math.sin(theta)
    return (x, y)


i = 0
num_in_row = 0

print("{")
for c in chars:
    rect_coords = []
    polar_coords = []
    i += 1
    for y in range(len(c)):
        for x in range(len(c[y])):
            if (c[y][x] != ' '):

                local_x = x - 3
                local_y = 3 - y
                local_theta, local_mag = rect_to_polar((local_x, local_y))
                print("\t{"+str(local_theta)+", "+str(int(local_mag*MAGNITUDE_SCALE))+"},")
                
                display_x = local_x + x_shift
                display_y = local_y - y_shift
                display_theta, display_mag = rect_to_polar((display_x, display_y))
                rect_coords.append((display_x, display_y))
                polar_coords.append((display_theta, display_mag))
    print("},{")

    for coord in rect_coords:
        Xs.append(coord[0])
        Ys.append(coord[1])
    for coord in polar_coords:
        thetas.append(coord[0])
        magnitudes.append(coord[1])
    x_shift += SPACING
    num_in_row += 1
    if (num_in_row >= CHARS_PER_ROW):
        num_in_row = 0
        x_shift = -16
        y_shift += SPACING

#print(thetas)
#print(magnitudes)
fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(projection='polar') # or use plt.subplot(111, polar=True)
#ax.set_ylim(-1, 1)
# Plot the data using the scatter function
c = ax.scatter(thetas, magnitudes, s=30, marker='s')
#c = ax.scatter([int(a) for a in angles_deg], [int(m) for m in magnitudes], s=20, marker='s')
plt.show()
