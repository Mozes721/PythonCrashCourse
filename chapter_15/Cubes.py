from matplotlib import pyplot as plt
x_values = list(range(5001))
cubes = [x**3 for x in x_values]

plt.scatter(x_values, cubes, edgecolor='none', c=cubes, cmap=plt.cm.BuGn, s=40)
plt.title("Cubes", fontsize=24)
plt.xlabel("Values", fontsize=14)
plt.ylabel("Cubes of Values", fontsize=14)
plt.tick_params(axis='both', labelsize=14)
plt.axis([0,5100,0,5100**3])
plt.figure(figsize=(10,6))
plt.show()