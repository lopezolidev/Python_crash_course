basic_foods = "filet mignong", "curry chicken", "roasted salmon", "peppered mashed potatoes", "ratatouille"

for food in basic_foods:
    print(food)
'''
filet mignong
curry chicken
roasted salmon
peppered mashed potatoes
ratatouille
'''
'''
basic_foods[2] = "hamburger"

Traceback (most recent call last):
  File "path/to/file/Python_crash_course/part_1/working_w_lists/ch.4_exercises/4_12.buffet.py", line 6, in <module>
    basic_foods[2] = "hamburger"
    ~~~~~~~~~~~^^^
TypeError: 'tuple' object does not support item assignment
'''
basic_foods = "filet mignong", "cheese lamb", "roasted salmon", "vainilla flan", "ratatouille"
for food in basic_foods:
    print(food)
'''
filet mignong
cheese lamb
roasted salmon
vainilla flan
ratatouille
'''