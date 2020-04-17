thirtyone_days = ["January", "March", "May", "July", "August", "October", "December"]
thirty_days = ["April", "June", "September", "November"]
outlier_days = ["February"]
month = str(input("Enter your month here: "))
if month in thirtyone_days:
    print ("31 days")
elif month in thirty_days:
    print ("30 days")
elif month in outlier_days:
    print ("28 days or 29 days on a leap year")
else:
    print ("Please enter a month")