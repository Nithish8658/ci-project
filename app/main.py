raw = input("Enter a number: ")
try:
    number = int(raw)
except ValueError:
    print("Please enter a valid integer.")
    exit()
if number == 0:
    print("The number is zero.")
else:
    if number < 0:
        print("The number is negative.")
    else:
        print("The number is positive.")

    
    if number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")

