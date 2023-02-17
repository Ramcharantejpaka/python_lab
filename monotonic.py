a = []
n = int(input("Number of elements in array:"))
for i in range(0, n):
    l = int(input("~"))
    a.append(l)
print(a)


def isMonotonic(A):
    x, y = [], []
    x.extend(A)
    y.extend(A)
    x.sort()
    y.sort(reverse=True)
    if A == x or A == y:
        return True
    return False


if isMonotonic(a):
    print("is monotonic")
