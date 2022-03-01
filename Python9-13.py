#Ryan Zmuda
#SOFT 204 Open Source Programming
#Python 7
#9-13 OrderedDict Rewrite

from collections import OrderedDict

print("\n#9-13 OrderedDict Rewrite")

glossary = OrderedDict()
glossary['concatenation'] = 'method of combining strings'
glossary['whitespace'] = 'nonprinting characters'
glossary['float'] = 'any number with a decimal point'
glossary['tuple'] = 'an immutable list'
glossary['dictionary'] = 'a collection of key-value pairs, like this one'
glossary['string'] = 'a series of characters'
glossary['method'] = 'an action performed on a piece of data'
glossary['index'] = 'the position of a value'
glossary['append'] = 'a method that adds a new element to a list'
glossary['slice'] = 'a specific group of items in a list'

print()
for word, definition in glossary.items():
    print("*", word.title() + ":", definition + ".")