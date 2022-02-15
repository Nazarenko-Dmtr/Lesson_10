from random import randint

def rect_drawer (slen, llen):
    return slen*"*" + ("\n" + ("*" + (" " * (slen-2)) + "*"))*(llen-2) + ("\n" + slen*"*")

print(rect_drawer (randint (2, 10), randint (2, 10)))