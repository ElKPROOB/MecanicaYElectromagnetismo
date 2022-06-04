from PIL import Image
import os

from matplotlib import image
import numpy as np
import matplotlib.pyplot as plt

img = Image.open(os.path.join('Calcular-Angulo', 'imagen' + '.jpg'))
fig, ax = plt.subplots(figsize=(8, 6))
ax.imshow(img, vmin=0, vmax=1)
plt.show()
