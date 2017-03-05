#! /usr/bin/env python2

from gimpfu import *

# Add a clipping mask layer

def python_add_clipping_mask_layer(img,layer):

    # Group undo start
    pdb.gimp_image_undo_group_start(img)

    # Save context
    pdb.gimp_context_push()

    # Get the current image's dimensions
    width = pdb.gimp_image_width(img)
    height = pdb.gimp_image_height(img)

    # Select the alpha of current layer
    layer_current = pdb.gimp_image_get_active_layer(img)
    pdb.gimp_context_set_antialias(1)
    pdb.gimp_context_set_feather(0)
    pdb.gimp_image_select_item(img,2,layer_current)

    # Create new layer
    layer_clip=pdb.gimp_layer_new(
            img,width,height,RGBA_IMAGE,"Clipping layer",100,NORMAL_MODE
            )
    pdb.gimp_image_insert_layer(img,layer_clip,None,0)
    pdb.gimp_drawable_fill(layer_clip,TRANSPARENT_FILL)
    pdb.gimp_image_set_active_layer(img,layer_clip)

    # Add empty mask to new layer
    layer_mask = pdb.gimp_layer_create_mask(layer_clip,4)
    pdb.gimp_layer_add_mask(layer_clip,layer_mask)
    pdb.gimp_selection_none(img)
    pdb.gimp_layer_set_edit_mask(layer_clip,0)

    # Restore context
    pdb.gimp_context_pop()

    # Group undo end
    pdb.gimp_image_undo_group_end(img)

register(
        "python_fu_add_clipping_mask_layer",
        "Add a clipping mask layer",
        "Add a clipping mask layer",
        "Haziq Noor Ariff",
        "Haziq Noor Ariff",
        "Apr 2016",
        "<Image>/Layer/Add a clipping mask layer",
        "",
        [],
        [],
        python_add_clipping_mask_layer)

main()
