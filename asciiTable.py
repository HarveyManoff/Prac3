

def main():
    result = get_number(2,66)
    #MIN_INPUT = 1
    #MAX_INPUT = 12

    #user_input = str(input("Enter a character: "))
    #CONV_NUMBER = ord(user_input)
    #print("The ASCII code for {} is {}".format(user_input, CONV_NUMBER))

    #USER_NUM = int(input("Please enter a valid number between {} and {}: ".format(MIN_INPUT, MAX_INPUT)))
    #while USER_NUM < MIN_INPUT or USER_NUM > MAX_INPUT:
    #USER_NUM = int(input("Please enter a valid number between {} and {}: ".format(lower, upper)))
    CONV_SYM = chr(result)
    print("The Character for {} is {}".format(result, CONV_SYM))

    for i in range(33, 128):  # how to make this inclusive?
        print("{0}  {1:>5}".format(i, chr(i)))
    return()
def get_number(lower,upper):
    correct_number = False
    result = 0
    while not correct_number:
        try:
            result = int(input("Enter a number ({}-{})".format(lower,upper)))
            correct_number = True
        except ValueError:
            print("Please enter a valid Numer!.")
    return(result)
main()