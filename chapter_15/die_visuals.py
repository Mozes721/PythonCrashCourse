import pygal
from chapter_15.die import Die

die = Die()


results = [die.roll() for roll_dice in range(1000)]


frequencies = [results.count(value) for value in range(1,  die.num_sides+1)]

hist = pygal.Bar()

hist._title = "Results of rolling one D6 1000 times."
hist.x_labels = ['1','2','3','4','5','6']
hist._x_title = "Results"
hist._y_title = "Frequencies of Results"

hist.add('D6'+ 'D6', frequencies)
hist.render_to_file('die_visual.svg')
