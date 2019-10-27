"""
Kolton Chiu
The caesar cypher takes in a string input from user
and changes each letter by the shift the user inputs
at the beginning. 
https://www.w3schools.com/python/ref_func_chr.asp
https://www.w3schools.com/python/ref_func_ord.asp
https://www.w3schools.com/python/ref_string_isupper.asp
https://www.w3schools.com/python/ref_string_islower.asp
"""
#variables
max_key = 26
lower_adjust = 97
higher_adjust = 65

#User input
shift = int(input(""))
text = str(input("plaintext: "))

#function that encrypts message
def caesar(text, shift):
    cipher = ""
    #loops through text input
    for i in range(len(text)):
        letter = text[i]
        #checks if letter is upper or lower case or neither
        if (letter.islower()):
            cipher = cipher + chr((ord(letter) + shift - lower_adjust) % max_key + lower_adjust) 
        elif (letter.isupper()):
            cipher = cipher + chr((ord(letter) + shift - higher_adjust) % max_key + higher_adjust)
        else:
            cipher = cipher + letter
    print ("ciphertext: " + str(cipher) + "\n")

#runs function    
caesar(text, shift)
