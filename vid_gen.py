from PIL import Image
from datetime import datetime
import numpy as np
import random

# http://giflib.sourceforge.net/whatsinagif/bits_and_bytes.html

def gif_gen (m, n, f):
	# let m and n be the standard notation for the size of a matrix and let f be the frames of the desired video.

	frames = []
	path = 'data/' + str(datetime.now()) + '.gif'

	for i in range(f):
		vals = np.random.rand(m, n, 3) * 255
		im = Image.fromarray(vals.astype('uint8')).convert('RGBA')

		frames.append(im)

	frames[0].save(path, save_all=True, append_images=frames[1:], optimize=False)

				
gif_gen(100,100,50)
