#! /usr/bin/env python2

from gimpfu import *

# Add an empty layer mask

def python_add_empty_layer_mask(img,layer):

    # Group undo start
    pdb.gimp_image_undo_group_start(img)

    # Get the current active layer
    layer_edit = pdb.gimp_image_get_active_layer(img)

    # Add empty mask to active layer
    layer_mask = pdb.gimp_layer_create_mask(layer_edit,0)
    pdb.gimp_layer_add_mask(layer_edit,layer_mask)

    # Set default colors
    pdb.gimp_context_set_default_colors()

    # Group undo end
    pdb.gimp_image_undo_group_end(img)

register(
        "python_fu_add_empty_layer_mask",
        "Add an empty layer mask",
        "Add an empty layer mask",
        "Haziq Noor Ariff",
        "Haziq Noor Ariff",
        "Apr 2016",
        "<Image>/Layer/Add an empty layer mask",
        "",
        [],
        [],
        python_add_empty_layer_mask)

main()
