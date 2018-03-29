import imageio
import matplotlib.pyplot as plt
import Image
import numpy as np

im = Image.new("RGB", (65,65), "white")
pic = np.array(im)
im=pic
imageio.imsave("white.png", im)

