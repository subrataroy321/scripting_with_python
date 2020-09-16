# open a file
subrata_file = open('subrata.txt', 'a')

numbers = [1,2,3]
for i in range(len(numbers)):
    num = numbers[i]
    subrata_file.write(f"{num}\n")


# write to file
#subrata_file.write("\nlearning scripting with python\n")

# read and print a file
#print(subrata_file.read())

# close a file
subrata_file.close()

adam_file = open('adam.txt', 'r+')
adam_file.write('\nHello Again n Again, Adam')
adam_file_lines = adam_file.readlines()
for i in range(len(adam_file_lines)):
    each_item = adam_file_lines[i]
    #print("Before: {}".format(each_item))
    print(each_item[0:-1])
    adam_file_lines[i] = each_item[0:-1]
    print(adam_file_lines)

adam_file.close()

## Look up how to read lines from a file in python