def solution(text, ending):
    if len(ending) > len(text):
        return False
    
    return text.endswith(ending)

print(solution( "fails",   "ails"))