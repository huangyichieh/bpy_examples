import bpy
import random
from mathutils import Vector

import sys
import os
blend_dir = os.path.basename(bpy.data.filepath)
if blend_dir not in sys.path:
   sys.path.append(blend_dir)
import utils


def createMetaball(origin=(0, 0, 0), n=30, r0=4, r1=2.5):
    metaball = bpy.data.metaballs.new('MetaBall')
    obj = bpy.data.objects.new('MetaBallObject', metaball)
    bpy.context.collection.objects.link(obj)

    metaball.resolution = 0.2
    metaball.render_resolution = 0.05

    for i in range(n):
        location = Vector(origin) + Vector(random.uniform(-r0, r0) for i in range(3))

        element = metaball.elements.new()
        element.co = location
        element.radius = r1

    return metaball


if __name__ == '__main__':
    # Remove all elements
    utils.removeAll()

    # Create camera
    target = utils.target()
    camera = utils.camera((-10, -10, 10), target)

    # Create lamps
    utils.rainbowLights(10, 100, 3, 250)

    # Create metaball
    metaball = createMetaball()

    # Render scene
    utils.renderToFolder('rendering', 'metaballs', 500, 500)
