import cipher
import setup
import lists
import secrets 

alphabet = lists.alphabet_list()
message, keyword = cipher.encryption_startup()

if keyword == 0:
    keyword, loaded_keyword = cipher.start_randomizer()

loaded_keyword = setup.assign_lists(keyword)
encrypted_message = cipher.encryption(message, loaded_keyword, keyword, alphabet)
print(f"Your encrypted message: {encrypted_message}")






