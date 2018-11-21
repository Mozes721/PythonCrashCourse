import pygal
from chapter_15.die import Die

die1 = Die()
die2 = Die()

results = [die1.roll() + die2.roll for roll_dice in range(1000)]

max_result = die1.num_sides + die2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]

hist = pygal.Bar()

hist._title = "Results of rolling one D6 1000 times."
hist.x_labels = ['1','2','3','4','5','6','7','8','9','10','11','12']
hist._x_title = "Results"
hist._y_title = "Frequencies of Results"

hist.add('D6'+ 'D6', frequencies)
hist.render_to_file('die_visual.svg')