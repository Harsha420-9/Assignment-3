def sum(my_list):
    Sum_List = 0
    for a in my_list:
        Sum_List += a
    return Sum_List

my_list=list(map(int,input("provide List of numbers with space : ").split()))
x = sum(my_list)
print("Sum of the list is : ",x)