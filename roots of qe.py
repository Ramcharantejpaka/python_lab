print("let the QE ax^2 + bx + c")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

d = (b ** 2) - (4 * a * c)
if d > 0:
    x1 = (-b + (d ** 0.5)) / (2 * a)
    x2 = (-b - (d ** 0.5)) / (2 * a)

    print("Real and distinct roots are ", x1, x2)
elif d == 0:
    x = -b / (2 * a)
    print("Equal roots", x)
else:
    print("Imaginary roots")
