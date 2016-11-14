word = "Triangulo"


def reverse(word):
    length = len(word) - 1
    reversedWord = ""
    e = length-1

    for i in range(length):
        reversedWord += word[e]
        e = e-1

    return reversedWord


reversedWord = reverse(word)
print(reversedWord)
