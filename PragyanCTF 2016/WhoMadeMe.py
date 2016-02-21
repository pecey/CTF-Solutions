import pickle
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

pixels = pickle.load(open("pixels.jpg.pkl","rb"))
# pixels contains co-ordinates of black pixels

pixels = pixels[1:]
with open("pixels_data.txt", "w") as f:
	for pixel in pixels:
		x,y = pixel
		f.write(str(x)+" "+str(y)+"\n")

x,y = np.loadtxt('pixels_data.txt').T
# Now x is a list of all x co-ordinates and y is a list of all y co-ordinates

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

# Scatter all the x and y co-ordinates on the graph
for x0,y0 in zip(x,y):
	ax.scatter(x0,y0)

plt.show()