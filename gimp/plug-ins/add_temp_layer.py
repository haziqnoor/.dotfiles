#! /usr/bin/env python2

from gimpfu import *

# Add a temporary layer

def python_add_temp_layer(img,layer):

    # Get the current image's dimensions
    width = pdb.gimp_image_width(img)
    height = pdb.gimp_image_height(img)

    # New temp layer
    layer_temp=pdb.gimp_layer_new(
            img,width,height,RGBA_IMAGE,"Temporary layer",100,NORMAL_MODE
            )
    pdb.gimp_image_insert_layer(img,layer_temp,None,0)
    pdb.gimp_drawable_fill(layer_temp,TRANSPARENT_FILL)

register(
        "python_fu_add_temp_layer",
        "Add a temporary layer",
        "Add a temporary layer",
        "Haziq Noor Ariff",
        "Haziq Noor Ariff",
        "Apr 2016",
        "<Image>/Layer/Add a temporary layer",
        "",
        [],
        [],
        python_add_temp_layer)

main()
