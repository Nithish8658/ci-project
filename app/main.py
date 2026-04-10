input=int(input("Enter a number: "))
if input!= int:
    print("Please enter a valid integer.")
    exit()
if input > 0:
    print("The number is positive.")
if input % 2 == 0:
    print("The number is even.")    
else:
    print("The number is odd.")
