def reverse(string):
    if len(string) == 1:
        return string
    else:
        return reverse(string[1:]) + string[0]


s = str(input("Enter the string: "))
print(reverse(s))
# without recursion
print(s[::-1])
