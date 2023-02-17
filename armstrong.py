# armstrong or not

num = int(input("enter any number"))
order = len(str(num))
print("order:",order)

temp = num
sum = 0
while temp > 0:
    digit = temp%10
    sum += digit ** order
    temp //= 10
print("sum:",sum)
if sum == num:
    print(num," is an armstrong number")
else:
    print(num," is not an armstrong number")

# armstrong number between the given sires

i = int(input("enter the starting number in series:"))
j = int(input("enter the range:"))

for k in range(i,j):
    temp = k
    order = len(str(temp))
    sum1 = 0
    while temp > 0:
        digi = temp % 10
        sum1 += digi ** order
        temp //= 10
    if sum1 == k:
        print(k)