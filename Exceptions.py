try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
except ValueError:
    print("Numerator and denominator must be valid numbers!")  #Will give an error with the values entered are not int
except ZeroDivisionError:
    print("Cannot divide by zero!")  #Will give an error with user enters 0 as the denominator
    print("Finished.")
