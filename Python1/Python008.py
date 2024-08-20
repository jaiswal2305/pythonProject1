
for x in range(1,101):
    if (x%5==0 and x%3==0):
        print(f"{x}fizzbuzz")
    elif (x%5==0):
        print(f"{x}Buzz")
    elif (x%3==0):
        print(f"{x}fizz")
    else:
        print(x)