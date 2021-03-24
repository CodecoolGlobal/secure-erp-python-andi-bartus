import random
import string

def generate_id():
    small_letter = random.choice(string.ascii_lowercase)
    small_letter2 = random.choice(string.ascii_lowercase)
    small_letter3 = random.choice(string.ascii_lowercase)
    small_letter4 = random.choice(string.ascii_lowercase)
    upper_letter = random.choice(string.ascii_uppercase)
    upper_letter2 = random.choice(string.ascii_uppercase)
    digit = random.choice([str(num) for num in range(10)])
    digit2 = random.choice([str(num) for num in range(10)])
    special = random.choice(["_","+","-","!"])
    special2 = random.choice(["_","+","-","!"])

    return(small_letter + special + digit + upper_letter + special2 + upper_letter2 + digit2 + small_letter2 +
           small_letter3 + small_letter4)
