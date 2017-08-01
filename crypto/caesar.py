from helpers import alphabet_position,rotate_character


def rotate_string_13(text):

    rotated = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    for char in text:
        rotated_idx = (alphabet_position(char) + 13) % 26
        if char.isupper():
            rotated = rotated + alphabet[rotated_idx].upper()
        else:
            rotated = rotated + alphabet[rotated_idx]

    return rotated



def rotate_string(text, rot):

    rotated = ''

    for char in text:
        if (char.isalpha()):
            rotated = rotated + rotate_character(char, rot)
        else:
            rotated = rotated + char

    return rotated
def main():
    from sys import argv, exit
    avg=["5"]
    print("This is what the user typed on the command line:", argv)

    text=input("Type a message")

    try:
        rot=int(input("Rotate by"))
        if rot.is_digit():
              print(rotate_string(text,rot))

    except ValueError:
            print("Opps! That's not a valid number.Try again")


            main()

if __name__=="__main__":
    main()
