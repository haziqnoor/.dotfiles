#! /usr/bin/env python2

from gimpfu import *

# Add a glaze layer

def python_add_glaze_layer(img,layer):

    # Get the current image's dimensions
    width = pdb.gimp_image_width(img)
    height = pdb.gimp_image_height(img)

    # Add glaze layer
    layer_glaze=pdb.gimp_layer_new(
            img,width,height,RGBA_IMAGE,"Glaze layer",100,MULTIPLY_MODE
            )
    pdb.gimp_image_insert_layer(img,layer_glaze,None,0)
    pdb.gimp_drawable_fill(layer_glaze,TRANSPARENT_FILL)

register(
        "python_fu_add_glaze_layer",
        "Add a glaze layer",
        "Add a glaze layer",
        "Haziq Noor Ariff",
        "Haziq Noor Ariff",
        "Apr 2016",
        "<Image>/Layer/Add a glaze layer",
        "",
        [],
        [],
        python_add_glaze_layer)

main()
