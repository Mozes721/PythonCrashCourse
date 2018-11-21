import matplotlib.pyplot as plt
from chapter_15.random_walk import RandomWalk

rw = RandomWalk()
rw.fill_walk()
plt.scatter(rw.x_values,rw.y_values, s=15)
plt.show()

point_numbers = list(range(rw.num_points))
plt.plot(rw.x_values, rw.y_values, c=point_numbers,cmap=plt.cm,edgecolors='Blue', s=15, linewidth = 5000)
plt.show()


