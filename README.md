# ray-tracing-basics
Simple repo to introduce the fundamental concepts of ray tracing

Ray tracing in game engines is the means by which graphics are rendered. At their core, a ray tracing algorithm is simply drawing a straight line between two objects in a scene and applying an interaction function. The ray tracing engine sends a ray into the scene, the ray intersects with an object, the ray is reflected back. In games, rays are almost always representing visible light and cast from the player into the scene and returned as an image. Hence, the name. 

The general operation of a ray tracer follows:
  - anywhere from 1000s to 1,000,000a of rays are drawn, or "cast," into the scene between the player and an object
  - the physics engine modifies the properties of each ray according to the properties of the object, e.g., an object looking darker in dim light
  - the rays are reflected back to the source
  - the physics engine interprets the reflected rays
  - all rays are aggregated to form a final image

However, we can apply custom physics and scene properties to simulate interactions between any objects with ray tracing. The ray tracer essentially links two objects together with a ray, and the effects they have on each other are captured by the physics engine. For example, a wifi network can be modeled using the Godot ray tracer, with "rays" as wifi signals with custom functions inside the physics engine. This repo breaks down the ray tracing process and highlights its utility in non-gaming applications. 

*This repo is laid out as follows:*
1. bare-bones-raytracing: a repo of the most basic type of ray tracing - drawing a line between objects and adding some physics

