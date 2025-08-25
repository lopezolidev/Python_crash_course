def double_char(s):
    str = ''
    for c in iter(s):
        str += c
        str += c
    return str 

print(double_char('Hello World!'))