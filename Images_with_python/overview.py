from PIL import Image

mac = Image.open('/home/bibek/git/python_scripting/Images_with_python/example.jpg')

# Note this is a specialized file type from PIL (pillow)
print(type(mac))
print(mac, mac.size, mac.filename)

# cropping Images
crop = mac.crop((0,0,100,100))

# Start at top corner (0,0)
x = 0
y = 0

# Grab about 10% in y direction , and about 30% in x direction
pencils = Image.open("/home/bibek/git/python_scripting/Images_with_python/pencils.jpg")
w = 1950/3
h = 1300/10

pencils.crop((x,y,w,h))

halfway = 1993/2
x = halfway - 200
w = halfway + 200
y = 800
h = 1257
mac_computer = mac.crop((x,y,w,h))

# Copying and Pasting Images

mac.paste(im=mac_computer,box=(0,0))
mac.paste(im=mac_computer,box=(796,0))

# Resizing
h,w = mac.size
new_h = int(h/3)
new_w = int(w/3)
# Note this is not permanent change
# for permanent change, do a reassignment
# e.g. mac = mac.resize((100,100))
mac.resize((new_h,new_w))

# Rotating Images
pencils.rotate(90)
# You can optionally pass in the expand parameter to fill the new rotated image to the old dimensions.
pencils.rotate(90,expand=True)

# Transparency
red = Image.open('/home/bibek/git/python_scripting/Images_with_python/red_color.jpg')
blue = Image.open('/home/bibek/git/python_scripting/Images_with_python/blue_color.png')
red.putalpha(128)
blue.putalpha(128)
blue.paste(red,box=(0,0),mask=red)
print(blue)
blue.save("/home/bibek/git/python_scripting/Images_with_python/purple.png")