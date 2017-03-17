##Prac 2 files ex


USER_NAME = input("Please enter your name: ")
output_file = open("name.txt", "w")
output_file.write(USER_NAME)


output_file.close()

input_file = open("name.txt","r")
READ_NAME = input_file.readline()
input_file.close()
print("You name is {}".format(READ_NAME))


num_list = ['17', '42']
num_file = open("numbers.txt","w")
for word in num_list:
    num_file.write(word +'\n')
num_file.close()

input_file = open("numbers.txt","r")
first_num = int(input_file.readline())
#print(first_num)
second_num = int(input_file.readline())
num_file.close()

answer = first_num + second_num
print(answer)