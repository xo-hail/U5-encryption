import random

""" Correct alphabet positions for program's reference. """

def alphabet_list():
    alphabet_list = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g',
        'h', 'i', 'j', 'k', 'l', 'm', 'n', 
        'o', 'p', 'q', 'r', 's', 't', 'u',
        'v', 'w', 'x', 'y', 'z'
    ]

    return alphabet_list

""" Assigns generated lists into the letters of the keyword. """

def assign_lists(keyword):
    alphabet = alphabet_list()
    loaded_keyword = {}

    for letter in keyword:
        shuffled_list = random_list()
        loaded_keyword[letter] = shuffled_list

    return loaded_keyword

""" Generates a random keyword. """

def random_keyword(alphabet_list):
    keyword = []
    keyword_length = 5

    while len(keyword) < keyword_length:
        number = random.randint(0, 25)
        keyword.append(alphabet_list[number])

    return keyword

""" Generates a random list intended for each letter of the keyword. """

def random_list():
    alphabet = alphabet_list()
    letter_list = []
    number_list = []

    while len(letter_list) < len(alphabet):

        # Main randomization
        number = random.randint(0, 25)

        # Anti-dupe system
        if number not in number_list:
            number_list.append(number)
        else:
            continue

        
        letter_list.append(alphabet[number])

    return letter_list



