


import math

def cylinderSurfaceArea(radius, height):
    surfaceArea = 2*math.pi*radius*(radius+height)
    print(f"The surface area of the cylinder is: {surfaceArea:.4f}")
    return surfaceArea

def cylinderVolume(radius, height):
    volume = math.pi*math.sqrt(radius)*height
    print(f"The volume of the cylinder is: {volume:.4f}")
    return volume
