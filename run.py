from PIL import Image
from graphics import GraphWin, Point, Line
from math import sqrt


actual_dimensions = (8.2296, 16.4592)  # Dimensions of the field  in width and length (meters)

scale = 100  # 100 pixels per meter

def coord_sort(coordinates):
    return sqrt(coordinates[0]**2 + coordinates[1]**2)


def build_pointcloud(pixels, size, threshold=5):
    points = []
    for i in range(0, size[1]):
        for j in range(0, size[0]):
            p = pixels[j, i]
            if p[0] <= threshold and p[1] <= threshold and p[2] <= threshold:
                points.append([j, i])
    return points


def scale_pointcloud(ptcloud):
    # Find dimensions
    l_x, l_y = 100000000, 1000000000
    h_x, h_y = 0, 0
    for point in pointcloud:
        if point[0] < l_x:
            l_x = point[0]
        if point[0] > h_x:
            h_x = point[0]
        if point[1] < l_y:
            l_y = point[1]
        if point[1] > h_y:
            h_y = point[1]
    print(l_x, l_y, h_x, h_y)
    height = h_y - l_y
    width = h_x - l_x
    print(width, height)

    # Find meters / pixel
    w_mpp = actual_dimensions[1] / width
    h_mpp = actual_dimensions[0] / height
    print(w_mpp, h_mpp)
    for point in pointcloud:
        point[0] *= w_mpp * scale
        point[1] *= h_mpp * scale


reader = Image.open("map.png")
pix = reader.load()
print(reader.size)
pointcloud = build_pointcloud(pix, reader.size)

window = GraphWin(height=2000, width=2000, title="Point Map")

scale_pointcloud(pointcloud)

for point in pointcloud:
    Point(point[0], point[1]).draw(window)


# We use this line drawing for scale
Line(Point(100, 100), Point(100 + scale, 100)).draw(window)
Line(Point(100, 100), Point(100, 100 + scale)).draw(window)

while window.isOpen():
    pass
