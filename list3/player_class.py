class Player:
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

    def __init__(self, name: str):
        self.score = 0
        self.name = name

    def score_word(self, word: str, mult: int = 1):
        value = 0
        for c in word:
            value += self.scores[c]

        value = value * mult

        self.score += value


def parse_input(input: str) -> (str, int):
    input = input.split(',')
    if len(input) == 1:
        word = input.pop().strip().lower()
        return (word, 1)
    elif len(input) == 2:
        mul = input.pop().strip()
        if mul == "double":
            mul = 2
        elif mul == "triple":
            mul = 3
        else:
            mul = 1
        word = input.pop().strip().lower()
        return (word, mul)
    else:
        raise NotImplementedError("I couldn't be bothered to do more than\
worked previously")


player_count = int(input("Player count for this game: "))
players = []
for i in range(1, player_count + 1):
    name = input(f"Player {i} name: ")
    players.append(Player(name))

running = True
current_player = 0
while running:
    print(f"{players[current_player].name}'s turn")
    print("@exit - quit game, @scores - display scores, @skip - pass the turn")
    inp = input("Type word [,multiplier]: ")
    if inp == "@exit":
        running = False
    elif inp == "@scores":
        for x in players:
            print(f"{x.name}: {x.score}")
    elif inp == "@skip":
        current_player = (current_player + 1) % len(players)
    else:
        word, mul = parse_input(inp)
        players[current_player].score_word(word, mul)
        current_player = (current_player + 1) % len(players)

print("Game over! Final scores:")
for x in players:
    print(f"{x.name}: {x.score}")
