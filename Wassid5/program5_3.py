from cylinderequations import cylinderSurfaceArea, cylinderVolume
from cylinderoaram import getRadius, getHeight

radius = getRadius()
height = getHeight()
cylinderSurfaceArea(radius, height)
cylinderVolume(radius, height)