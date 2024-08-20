Year=int(input("Enter an year to check if it is leap year"))
if (Year%4==0) and Year%100!=0 or Year%400==0 :
    print("This is leap year")
else:
    print("This is not a leap year")