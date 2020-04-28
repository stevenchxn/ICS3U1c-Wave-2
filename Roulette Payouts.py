import random
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
list = [00, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 28, 29, 30, 31, 32, 33, 34, 35, 36]
number = random.choice(list)

print(number)
if number == 0 or 00:
    if number == 0:
        print ("Pay ", 0)
    else:
        print ("Pay ", 00)
else:
    print ("Pay ", number)
    if number in red:
        print ("Pay red")
    else:
        print ("Pay black")
            
    if (number % 2) == 0:
        print ("Pay even")
    else:
        print ("Pay odd")
        
    if number <= 18:
        print ("Pay 1 to 18")
    else:
        print ("Pay 19 to 36")