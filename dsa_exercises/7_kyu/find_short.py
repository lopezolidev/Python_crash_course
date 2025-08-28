def find_short(s):
    words = s.split(' ')
    words = sorted(words, key = len)
    l = len(words[0])
    return l # l: shortest word length

arg = "bitcoin take over the world maybe who knows perhaps"

print(find_short(arg))