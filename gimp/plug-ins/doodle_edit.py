#! /usr/bin/env python2

from gimpfu import *

# Edit existing doodles

def python_doodle_edit(img,layer,newcolor,oldcolor):
    # Group undo start
    pdb.gimp_image_undo_group_start(img)

    # Save context
    pdb.gimp_context_push()

    # Get the current image's dimensions
    width = pdb.gimp_image_width(img)
    height = pdb.gimp_image_height(img)

    # New background
    layer_newbg = pdb.gimp_layer_new(
            img,width,height,RGBA_IMAGE,"new bg",100,NORMAL_MODE
            )
    pdb.gimp_image_insert_layer(img,layer_newbg,None,1)

    # New background fill color
    pdb.gimp_context_set_background(newcolor)
    pdb.gimp_drawable_fill(layer_newbg,BACKGROUND_FILL)

    # Return to original layer
    pdb.gimp_image_set_active_layer(img,layer)
    pdb.plug_in_colortoalpha(img,layer,oldcolor)

    # Restore context
    pdb.gimp_context_pop()

    # Group undo end
    pdb.gimp_image_undo_group_end(img)

    # Set default colors
    pdb.gimp_context_set_default_colors

register(
        "python_fu_doodle_edit",
        "Edit existing doodle",
        "Edit existing doodle",
        "Haziq Noor Ariff",
        "Haziq Noor Ariff",
        "Sep 2014",
        "<Image>/File/Doodle/Edit Doodle...",
        "*",
        [
            (PF_COLOR, "newcolor", "New background color", (128,128,128)),
            (PF_COLOR, "oldcolor", "Remove old background color", (128,128,128))
        ],
        [],
        python_doodle_edit)

main()
