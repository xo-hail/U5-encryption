import setup

alphabet_list = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k', 'l', 'm', 'n', 
    'o', 'p', 'q', 'r', 's', 't', 'u',
    'v', 'w', 'x', 'y', 'z'
    ]


""" Encrypts a message passed into the function. """

def encryption(message, loaded_keyword, keyword, alphabet_list):
    clean_msg = message_cleaning(message)
    encrypted_msg = []


    for letter in clean_msg:   
        letter_index = alphabet_list.index(letter)

        while encrypted_msg < len(clean_msg):

            for letter in keyword:
                letter_list = loaded_keyword[letter]
                letter_replacement = letter_list[letter_index]

                encrypted_msg.append(letter_replacement)

    return encrypted_msg

def decryption(encrypted_msg, loaded_keyword):

    return

def message_cleaning(message):
    cleaned_message = message.lower().strip()
    split_cleaned_msg = cleaned_message.split()

    return split_cleaned_msg

