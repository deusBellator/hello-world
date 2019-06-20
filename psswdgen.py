#random password generator

import random
import string


def pw_gen(size, chars=string.ascii_letters + string.digits + string.punctuation + string.ascii_lowercase + string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range(size))

name = input('What is your username?')
print ('Your username is %s' % (name))


print (pw_gen(int(input("How many characters in your password? "))))
print ('Is your new password ')
