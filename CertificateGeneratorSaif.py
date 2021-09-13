from PIL import Image, ImageDraw, ImageFont
import pandas as pd

with open('names.txt', 'r') as f:
	names = f.read()
	names = names.strip()

names = names.split(',')
#dummy = "Saif Khan"
for name in names:
	im = Image.open("SampleCert.png")
	d = ImageDraw.Draw(im)
	location = (1217, 1378)
	text_color = (0, 0, 0)
	font = ImageFont.truetype("arial.ttf", 150)
	d.text(location, name, fill=text_color, font=font)
	im.save("SampleInput/Certificate_" + name + ".pdf")
