'''
1) Write a function that takes a list of strings an prints them, one per line, in a rectangular frame.
For example the list ["Hello", "World", "in", "a", "frame"] gets printed as:

*********
* Hello *
* World *
* in    *
* a     *
* frame *
*********
'''
def frame(list_A):
    print("Given list is: ", list_A)
    max_len = 0
    for i in list_A:
        length = len(i)
        if length > max_len:
            max_len = length
        else:
            pass

    #print(max_len)
    final_len = max_len + 4
    print()
    print("*" * (final_len))
    for i in list_A:
        list1 = len(i)
        space = final_len - (list1 + 1)
        print("* " + i, end="")
        print(""*space + " " * (final_len - (len(i) + 3)) + "*")

    print("*" * final_len)

list_A = input("Enter a line:")
list_A = list_A.split(" ")
frame(list_A)
