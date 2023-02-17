import math

print("welcome")

# addition of two numbers
print("enter two numbers")
a = input("num1:")
b = input("num2:")
c = int(a) + int(b)
print(c)

# fibonacci series
n1, n2 = 0, 1
count = 0
n = int(input("enter range"))

if n <= 0:
    print("Please enter a positive integer")

elif n == 1:
    print("Fibonacci sequence: ", n)

else:
    print("Fibonacci sequence:")
    while count < n:
        print(n1)
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        count += 1


# ascii value of a character
a1 = input("enter a character: ")
print(ord(a1))

# area of triangle
print("enter sides of a triangle:")
s1 = int(input("side1:"))
s2 = int(input("side2:"))
s3 = int(input("side3:"))

p = s1 + s2 + s3
area = math.sqrt(p * (p - s1) * (p - s2) * (p - s3))
print("area =", area)

# sum of digits
num = int(input("enter any number:"))
sum = 0
while num != 0:
    sum = sum + (num % 10)
    num //= 10
print("sum =", sum)

# area of circle
r = int(input("enter radius of circle:"))
area = math.pi * r * r
print("are of circle =", area)
