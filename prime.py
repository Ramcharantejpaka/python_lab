# is prime or not
p = int(input("enter any number:"))
if p > 1:
    for i in range(2, p):
        if (p % i) == 0:
            print(p, "is not a prime number")
            break
    else:
        print(p, "is a prime number")
else:
    print("enter positive integer")

# prime numbers in given series

print("enter the range:")
i = int(input("start:"))
j = int(input("end:"))


def isPrime(k):
    for l in range(2, k):
        if (k % l) == 0:
            return False
    else:
        return True


for m in range(i, j):
    if isPrime(m):
        print(m)
