#! /usr/bin/env python2

from gimpfu import *

# Create new doodle file

def python_doodle_new(width,height,color):
    # Make a new image
    img = gimp.Image(width,height,RGB)

    # Save context
    pdb.gimp_context_push()

    # Create new "bg" layer
    layer_bg = gimp.Layer(img,"bg",width,height,RGB_IMAGE,100,NORMAL_MODE)
    img.add_layer(layer_bg)
    gimp.set_background(color)
    layer_bg.fill(BACKGROUND_FILL)

    # Create new "ink" layer
    layer_ink = pdb.gimp_layer_new(
            img,width,height,RGBA_IMAGE,"ink",100,NORMAL_MODE
            )
    img.add_layer(layer_ink,-1)

    # Create a new image window
    gimp.Display(img)

    # Show the new image window
    gimp.displays_flush()

    # Restore context
    pdb.gimp_context_pop()

register(
        "python_fu_doodle_new",
        "Create new doodle file",
        "Create new doodle file",
        "Haziq Noor Ariff",
        "Haziq Noor Ariff",
        "Sep 2014",
        "New Doodle...",
        "",
        [
            (PF_INT32, "width", "Width (px)", 1200),
            (PF_INT32, "height", "Height (px)", 1000),
            (PF_COLOR, "color", "Background color", (128,128,128)),
        ],
        [],
        python_doodle_new,
        menu="<Image>/File/Doodle"
        )

main()
