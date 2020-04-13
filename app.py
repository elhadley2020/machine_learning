import numpy
import matplotlib.pyplot
from mpl_toolkits.mplot3d import Axes3D

# length of list
obs = 1000
#generate x list
xs = numpy.random.uniform(low = -10, high= 10, size = (obs, 1))
#generate z list
zs = numpy.random.uniform(low = -10, high= 10, size = (obs, 1))
#combine lists in to multi dim list
inputs = numpy.column_stack((xs,zs))

#generator list for noise
noise = numpy.random.uniform(-1,1,(obs,1))

targets = 2*xs - 3*zs + 5 + noise

targets = targets.reshape(obs,)
fig = matplotlib.pyplot.figure()
ax = fig.add_subplot(111,projection='3d')
ax.plot(xs,zs,targets)
ax.set_xlabel('xs')
ax.set_ylabel('zs')
ax.set_zlabel('Targets')
ax.view_init(azim=100)
matplotlib.pyplot.show()
targets = targets.reshape(obs,1)

