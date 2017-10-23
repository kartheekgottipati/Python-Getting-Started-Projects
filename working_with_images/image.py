#!/usr/bin/python
# -*- coding: utf-8 -*-

from PIL import Image

try: 
	
	## Input Files 
	filename = "harvey.jpg"
	filename2 = "harvey2.jpg"

	## Retrieve size of image
	with Image.open(filename) as img:
		width, height = img.size

		## Rotating an Image
		img = img.rotate(180)
		
		## Save changes in image
		## Saved in the same relative location
		img.save("rotated_harvey.jpg")

		## Cropping an Image:
		area = (0, 0, width/2, height/2)
		img = img.crop(area)
		img.save("cropped_harvey.jpg")

		## Resizing an Image
		img = img.resize((width * 2, height * 2))
		img.save("resized_harvey.jpg")

		## Pasting an image on another image
		with Image.open(filename2) as img2:
			img.paste(img2, (150, 150))
			img.save("pasted_harvey.jpg")

        ## Getting a Histogram of an Image
       	img.histogram()

       	## Transposing an Image
       	transposed_img = img.transpose(Image.FLIP_LEFT_RIGHT)
        transposed_img.save("transposed_harvey.jpg")

        ## Split an image into individual bands
        img.split()

        ## tobitmap
        img.mode

        ## can only be used for mode “1” images
        ## Un comment the below 2 line if using 1 bit pixel black and white images.
        # print img.tobitmap()
        # print type(img.tobitmap())

        ## Creating a thumbnail
        img.thumbnail((200, 200))
        img.save("thumbnail.jpg")

except IOError:
    print(e.msg())
