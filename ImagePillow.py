from PIL import Image
im = Image.open('qrcode.png')
print(im.format,im.size,im.mode)
im.thumbnail((200,100))
im.save('thumb.png','JPEG')
