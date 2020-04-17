import math
a, b, c = input("Enter the variables a, b, c in the equation f(x) = ax^2 + bx + c: ").split()

print (f"You entered {a}x^2 + {b}x + {c}")

if (int(b) ** 2 - 4 * int(a) * int(c)) == 0:
    print ("This contains one real root: ", ((-b) / 2*a))

elif (int(b) ** 2 - 4 * int(a) * int(c)) > 0:
    r = (int(b) ** 2 - 4 * int(a) * int(c))
    x1 = ((-int(b) + math.sqrt(r))/(2*int(a)))
    x2 = ((-int(b) - math.sqrt(r))/(2*int(a)))
    print ("This contains two real roots: ", (x1, x2))

else:
    print ("This contains no real roots")