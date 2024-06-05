import bpy
import csv
import pathlib
import mathutils

# File paths
file_loc = pathlib.Path(__file__).parent.resolve()
folder = pathlib.Path(file_loc).parent.resolve()
parent_folder = pathlib.Path(__file__).parents[3]

# Construct the path to the CSV file
csv_file = pathlib.Path(folder).joinpath('report.csv')

# Create a new mesh object to hold all the circles
mesh = bpy.data.meshes.new(name="cylinders")
obj = bpy.data.objects.new("cylinders", mesh)
bpy.context.collection.objects.link(obj)

# Function to create a cylinder based on (x, y, z) coordinates, direction and radius
def create_cylinder(x, y, z, radius, direction):
    bpy.ops.mesh.primitive_cylinder_add(
        vertices=32,
        depth=0.2,
        radius=radius,
        location=(x, y, z)
    )
    
    # Get the newly created cylinder
    cylinder = bpy.context.object
    
    # Calculate the rotation to align the cylinder with the direction vector
    direction_vector = mathutils.Vector(direction).normalized()
    up_vector = mathutils.Vector((0, 0, 1))
    rotation_quat = up_vector.rotation_difference(direction_vector)
    
    # Apply the rotation
    cylinder.rotation_mode = 'QUATERNION'
    cylinder.rotation_quaternion = rotation_quat
    
    # Parent the new cylinder to the main object (if required)
    #cylinder.select_set(True)
    #bpy.context.view_layer.objects.active = obj
    #bpy.ops.object.parent_set(type='OBJECT')
    #cylinder.select_set(False)

# Open the CSV file and create cylinders for each line
with open(csv_file, newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)  # Skip the first line (header)
    for row in csv_reader:
        x, y, z, radius = map(float, [row[1], row[2], row[3], row[7]])
        direction = [float(row[4]), float(row[5]), float(row[6])]
        create_cylinder(x, y, z, radius, direction)
