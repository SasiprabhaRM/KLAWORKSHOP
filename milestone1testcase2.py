
import math
import numpy as np

def generate_wafer_points(wafer_diameter, num_points, angle_deg):
    radius = wafer_diameter / 2
    angle_rad = math.radians(angle_deg)
    points = []

    for i in range(num_points):
        theta = 2 * math.pi * i / num_points
        x = radius * math.cos(theta + angle_rad)
        y = radius * math.sin(theta + angle_rad)
        points.append((x, y))
    return points

# Read input values from file
with open("Testcase2.txt", "r") as file:
    lines = file.readlines()
    wafer_diameter = float(lines[0].split(":")[1].strip())
    num_points = int(lines[1].split(":")[1].strip())
    angle_deg = float(lines[2].split(":")[1].strip())

# Write points to file
with open("python2.txt", "w") as file:
    for point in generate_wafer_points(wafer_diameter, num_points, angle_deg):
        file.write(f"{point[0]},{point[1]}\n")

print("Points written to python2.txt")