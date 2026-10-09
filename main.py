import cipher
import sys

""" Start up the encryption system. """

def encryption_startup():
    if_startup = input("Greetings! Would you like to encode a message (yes/no)? ")

    if if_startup.strip().lower() == "yes":
        message = input("Paste your message here: ")
    else:
        sys.exit("See ya never!")

    if_has_keyword = input("Do you have a particular keyword in mind (yes/no)? ")


    return message



