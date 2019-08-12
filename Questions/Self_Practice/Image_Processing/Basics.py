import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import pickle

image_is = mpimg.imread("xyz.jpg")
pickle.dump(image_is, open("saved.p", "wb"))
plt.imshow(image_is)

