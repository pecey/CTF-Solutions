from PIL import Image
import struct

img = Image.open("landscape.png")
rows, cols = img.size
temp = ""

for i in range(0, rows, 7):
	rgb = img.getpixel((i,50))
	hex_code = struct.pack('BBB',*rgb).encode('hex')
	temp += hex_code[:2]

print temp.decode("hex")