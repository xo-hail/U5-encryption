import setup

alphabet_list = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k', 'l', 'm', 'n', 
    'o', 'p', 'q', 'r', 's', 't', 'u',
    'v', 'w', 'x', 'y', 'z'
    ]

""" Starts up the randomizer. """

def start_randomizer():
    keyword = setup.random_keyword(alphabet_list)
    loaded_keyword = setup.assign_lists(keyword)

    return keyword, loaded_keyword
    
""" Encrypts a message passed into the function. """

def encryption(message, loaded_keyword, keyword, alphabet_list):
    clean_msg = message_cleaning(message)
    encrypted_msg = []
    keyword_tracker = 0

    for char in clean_msg:   
        # 1. Takes the index of the character of the message from the original alphabet list
        letter_index = alphabet_list.index(char)

        # 2. The keyword tracker divides itself by the length of the keyword
        # -- This keeps the loop strictly within parameters
        current_keyword_letter = keyword[keyword_tracker % len(keyword)]

        # 3. The current keyword letter value is then used as the integer from within the letter list
        letter_list = loaded_keyword[current_keyword_letter]
        letter_replacement = letter_list[letter_index]

        # 4. The letter replacement is appended into the encrypted message
        encrypted_msg.append(letter_replacement)

        keyword_tracker += 1

    return encrypted_msg

def decryption(encrypted_msg, loaded_keyword):

    return

def message_cleaning(message):
    cleaned_message = message.lower().strip()
    split_cleaned_msg = cleaned_message.split()

    return split_cleaned_msg

