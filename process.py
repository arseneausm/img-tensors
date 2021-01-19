import numpy as np
from PIL import Image

def approx(path):
	im = Image.open(path)
	
	i, j = im.size		# 2
	k = im.n_frames		# +1

	dat = np.zeros((i,j,k))

	for frame in range(0, im.n_frames):
		for x in range(i):
			for y in range(j):
				val = im.getpixel((x, y))

				dat[x,y,frame] = val

	print(dat)


approx("data/20210119-020223.gif")
