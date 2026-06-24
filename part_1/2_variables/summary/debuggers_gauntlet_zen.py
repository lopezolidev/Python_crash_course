import this
'''
system_msg = 'Exploit execution failed on target's workstation'

print(system_msg)
print(systm_msg)

    system_msg = 'Exploit execution failed on target's workstation'
                                                                  ^
SyntaxError: unterminated string literal (detected at line 3)
'''

# fix

system_msg = "Exploit execution failed on target's workstation"
print(system_msg)

print(this)

# If the implementation is hard to explain, it's a bad idea.