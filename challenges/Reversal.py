def reverse(word):
    length = len(word) - 1
    reversed_word = ""
    reversed_character = length-1

    # 'for' loop to iterate through as many characters the word has
    for i in range(length):
        # Assigns the current character selected to the reversed_word variable
        reversed_word += word[reversed_character]
        # Countdowns from the last character of the word to reverse to the first
        reversed_character = reversed_character-1

    return reversed_word

if __name__ == "__main__":
    word = "Triangulo"
    reversed_word = reverse(word)

    print(reversed_word)
