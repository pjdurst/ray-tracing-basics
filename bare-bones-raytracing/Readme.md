*This repo contains a rundown on the most basic building blocks of a ray tracer and contains the following files:*

**read_mesh_from_file:**
A set of python functions for importing object meshes

**visualize_mesh:**
A set of python functions for diplaying objects

**edge-vertices-cube.txt:**
This is the simpliest mesh possible. It is a .txt file made up of geometric points. The vertices are the (x,y,z) coordinates that define the bournds of the object.
The edges are the line between each (x,y,z) bound. So in essence, a mesh is a collection of points and the lines connecting them. This mesh reprsents a simple, textureless cube.

**basic-raytracer:**
The most bare-bones ray tracer possible - a simple funtion to plot a 3D shape. The viewpoint is the user, e.g., the person executing the code. The mesh is a simple 3D cube. The "rendered image" is the plot displayed by matplotlib. This ray tracer contains no physics, so it doesn't really "project rays." Instead, it is meant to show the most basic ray tracing building blocks: a mesh to visualize, math functions to tell the code what and how to visualize, and a display to show the final image.

*usage: python3 basic-raytracer.py*

