from string import ascii_lowercase


def check(s):
    return set(ascii_lowercase) - set(s.lower()) == set([])


string = input("Enter string:")
if check(string):
    print("The string is a pangram")
else:
    print("The string isn't a pangram")
