m1 = int(input("enter mass 1:"))*(10**5)
m2 = int(input("enter mass 2:"))*(10**5)
d = int(input("enter the distance between objects"))
G = 6.6743 * (10**-11)
F = (G *m1*m2)/d**2
print(round(F,3),"N")