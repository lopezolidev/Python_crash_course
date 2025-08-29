import pizza

pizza.make_pizza_3(16, 'pepperoni')
pizza.make_pizza_3(12, 'mushrooms', 'green peppers', 'extra cheese')
# even though we call make_pizza_3 it calls all the other functions inside the
# module → this is because we have function calls inside pizza.py
# the interpreter reads whole pizza.py and executes function calls
# To execute code inside a module: module_name.function_name() 