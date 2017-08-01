def alphabet_position(character):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    lower = character.lower()
    return alphabet.index(lower)

def rotate_character(char, rot):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rotated_idx = (alphabet_position(char) + rot) % 26

    if char.isupper():
        return alphabet[rotated_idx].upper()
    else:
        return alphabet[rotated_idx]