scores = {
    'a': 1,
    'e': 1,
    'i': 1,
    'l': 1,
    'n': 1,
    'o': 1,
    'r': 1,
    's': 1,
    't': 1,
    'u': 1,
    'd': 2,
    'g': 2,
    'b': 3,
    'c': 3,
    'm': 3,
    'p': 3,
    'f': 4,
    'h': 4,
    'v': 4,
    'w': 4,
    'y': 4,
    'k': 5,
    'j': 8,
    'x': 8,
    'q': 10,
    'z': 10
}


def count(word: str, mult=1) -> int:
    value = 0
    for c in word:
        value += scores[c]

    value = value * mult
    return value


inp = input().split(',')

if inp.__len__() == 1:
    word = inp.pop().strip().lower()
    print(count(word))
elif inp.__len__() > 1:
    multiplier = inp.pop().strip()
    if multiplier == "double":
        multiplier = 2
    elif multiplier == "triple":
        multiplier = 3
    else:
        multiplier = 1

    word = inp.pop().strip().lower()
    print(count(word, multiplier))
