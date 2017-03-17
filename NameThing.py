def main():
    user_name = get_name()
    for i in range(0,len(user_name),2): #How do I do the last part for this?
        char = user_name[i]
        print("{}".format(char))
    return()


def get_name():
    GOOD_NAME = 0
    while GOOD_NAME == 0:
        user_name = input("Please enter your name: ")
        if not user_name:
            print("Please enter a valid name.")
        else:
            GOOD_NAME = 1
    return user_name


testr = main()