from PIL import Image
from graphics import GraphWin, Point, Line
from math import sqrt


actual_dimensions = (8.2296, 16.4592)  # Dimensions of the field  in width and length (meters)

scale = 50  # pixels per meter

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
    height = h_y - l_y
    width = h_x - l_x

    # Find meters / pixel
    w_mpp = actual_dimensions[1] / width
    h_mpp = actual_dimensions[0] / height
    for point in pointcloud:
        point[0] *= w_mpp * scale
        point[1] *= h_mpp * scale


reader = Image.open("map.png")
pix = reader.load()
pointcloud = build_pointcloud(pix, reader.size)

window = GraphWin(height=600, width=1000, title="Point Map")

scale_pointcloud(pointcloud)

for point in pointcloud:
    Point(point[0], point[1]).draw(window)


# We use this line drawing for scale
Line(Point(5, 5), Point(5 + scale, 5)).draw(window)
Line(Point(5, 5), Point(5, 5 + scale)).draw(window)

window.getMouse()
window.close()
