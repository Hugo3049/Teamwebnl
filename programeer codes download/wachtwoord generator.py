import string
import random

def pass_gen():

    s_l = string.ascii_lowercase
    s_u = string.ascii_uppercase
    s_d = string.digits
    s_p = string.punctuation

    # empty list
    pass_list = []

    # add chars to the list
    pass_list.extend(s_l)
    pass_list.extend(s_u)
    pass_list.extend(s_d)
    pass_list.extend(s_p)

    # shuffle password list chars (reorganize the order of the list items)
    random.shuffle(pass_list)

    # get password length frome user input
    pass_length = int(input('Kies een wachtwoord lengte:  '))

    # convert password list to string frome index 0 to password length enterd from user
    password_result = ''.join(pass_list[0:pass_length])
    # print gegenereerd wachtwoord

    print('Gegenereerd wachtwoord is: ',password_result)

# call gegenereerd wachtwoord functie
pass_gen()
