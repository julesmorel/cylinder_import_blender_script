import bpy
import csv
import pathlib

# File paths
file_loc = pathlib.Path(__file__).parent.resolve()
folder = pathlib.Path(file_loc).parent.resolve()
parent_folder = pathlib.Path(__file__).parents[3]

# Construct the path to the CSV file
csv_file = pathlib.Path(folder).joinpath('data.csv')

# Create a new mesh object to hold all the circles
mesh = bpy.data.meshes.new(name="cylinders")
obj = bpy.data.objects.new("cylinders", mesh)
bpy.context.collection.objects.link(obj)

# Function to create a cylinder based on (x, y, z) coordinates and radius
def create_cylinder(x, y, z, radius):
    bpy.ops.mesh.primitive_cylinder_add(
        vertices=32,
        depth=0.2,
        radius=radius,
        location=(x, y, z)
    )

# Open the CSV file and create cylinders for each line
with open(csv_file, newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)  # Skip the first line (header)
    for row in csv_reader:
        x, y, z, radius = map(float, [row[1], row[2], row[3], row[4]])
        create_cylinder(x, y, z, radius)
