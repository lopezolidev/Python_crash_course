glossary = {
    'Variable': '\n\t A memory address used to store a value',
    'For-loop': '\n\t A block of code that repeats under certain condition',
    'List': '\n\t A data structure that stores values in a linear fashion',
    'If statements': '\n\t A flow control structure that proceeds with a block of code if certain condition is met',
    'Dictionaries': '\n\t A data structre that stores values in a key-value format',
    'Function': '\n\t A block of organized, reusable code that performs a single, related action.',
    'Method': '\n\t A function that belongs to a class or an object and is called using dot notation.',
    'Tuple': '\n\t An immutable data structure that stores an ordered collection of values in parentheses.',
    'Boolean Expression': '\n\t An expression that evaluates to a value of either True or False.',
    'Module': '\n\t A file containing Python definitions and statements that can be imported into a program.'
}

for word, definition in sorted(glossary.items()):
    print(f"\n{word}")
    print(definition)