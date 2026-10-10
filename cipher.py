import setup
import lists 
import sys

""" Start up the encryption system. """

def encryption_startup():

    if_startup = input("Greetings! Would you like to encode a message (yes/no)? ")
    if if_startup.strip().lower() == "yes":
        message = input("Paste your message here: ")
    else:
        sys.exit("Aww.")

    if_has_keyword = input("Do you have a particular keyword in mind (yes/no)? ")
    if if_has_keyword.strip().lower() == "yes":
        keyword = input("What would you like your keyword to be? ")
    else:
        print("That's okay. We'll generate one for you :)")
        keyword = 0

    return message, keyword

""" Starts up the randomizer. """

def start_randomizer():
    keyword = setup.random_keyword(lists.alphabet_list())
    loaded_keyword = setup.assign_lists(keyword)

    return keyword, loaded_keyword
    
""" Encrypts a message passed into the function. """

def encryption(message, loaded_keyword, keyword, alphabet_list):
    clean_msg = message_cleaning(message)
    encrypted_msg = []
    keyword_tracker = 0

    for char in clean_msg: 

        if char in alphabet_list:  
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

        else:
            encrypted_msg.append(char)

    # Assemble the listed encrypted msg back together
    # You could have used the join function but to celebrate getting it right, you chose to keep your original logic
    joined_encrypted_msg = ""

    for char in encrypted_msg:
        joined_encrypted_msg += char


    return joined_encrypted_msg

def decryption(encrypted_msg, loaded_keyword):

    return

def message_cleaning(message):
    cleaned_message = message.lower().strip()

    return cleaned_message

