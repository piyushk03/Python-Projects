from PIL import Image
me = Image.open('photo .JPG')
bg = Image.open('Cruise-Origin-Dubai.webp')
bg.paste(me,(100,0),me)
bg.show()
