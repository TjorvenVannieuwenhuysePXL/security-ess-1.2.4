english_alphabet = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z'
]

def main():
    input_text = input("Provide the ciphered text: ").upper()

    current_mapping = {}
    print("Please provide the substitution mapping.\nIf a letter is unmapped, leave it empty.")

    for letter in english_alphabet:
        if letter not in input_text:
            continue

        provided_substitution = input(letter + " -> ")

        if not provided_substitution:
            continue

        current_mapping[letter] = provided_substitution

    trans = str.maketrans(current_mapping)
    translated_text = input_text.translate(trans)
    print(translated_text)

if __name__ == '__main__':
    main()