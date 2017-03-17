"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""
__author__ = 'Lindsay Ward'

MENU = "C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ (for quit)"
print(MENU)
choice = input(">>> ").upper()


def To_fahrenheit():
    global celsius, fahrenheit
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    #print("Result: {:.2f} F".format(fahrenheit))
    return(fahrenheit)

def To_Celcius():
    global fahrenheit, celsius
    fahrenheit = float(input("fahrenheit:  "))
    celsius = (5 / 9) * (fahrenheit - 32)
    #print("Result: {:.2f} C".format(celsius))
    return(celsius)

while choice != "Q":
    if choice == "C":
        To_fahrenheit()
    elif choice == "F":
        # TODO: Write this section so the program converts F to C and displays the result
        # Hint: celsius = 5 / 9 * (fahrenheit - 32)
        To_Celcius()
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")