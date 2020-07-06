from PIL import Image, ImageFilter

# img = Image.open('./pokedex/pikachu.jpg')
img = Image.open('./astro.jpg')
# .thumbnail changes the img and does not create a new one
img.thumbnail((400,200))
img.save('thumbnail.jpg')
# .thumbnail does not warp img the (400,200) is setting a max width and height
print(img.size)

# filtered_img = img.filter(ImageFilter.BLUR)

# filtered_img.save('blur.png','png')

# filtered_img = img.convert('L')
# crooked = filtered_img.rotate(90)
# resize = filtered_img.resize((300,300))
# box = (100,100,400,400)
# cropped = filtered_img.crop(box)
# cropped.save('grey.png','png')



