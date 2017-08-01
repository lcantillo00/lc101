from helpers import alphabet_position,rotate_character

def encrypt(text,key):
    encrypted=[]
    starting_index = 0
    for letter in text:
        rotation=alphabet_position(key[starting_index])
        if letter.isalpha():
            encrypted.append(rotate_character(letter,rotation))
        else:
            encrypted.append(letter)
        if starting_index==(len(key)-1):
            starting_index=0
        else:
            starting_index+=1
           
    return ''.join(encrypted)



def main():
    mytext=input("your text")
    try:
        myrot=input("put a clave")
        if myrot.isalpha():
             print(encrypt(mytext,myrot))


    except ValueError:
           
            print("Opps! That's not a valid number.Try again")
            main()
if __name__=="__main__":
    main()
