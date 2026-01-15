def reverse(lst):
    #Write a function named reverse which gets a list of numbers as argument and returns the reversed list.
    revlst = []
    for i in range(len(lst) -1,-1,-1):
        revlst.append(lst[i])
    return(revlst)

#Each test case has one input - an odd whole number.
#Your task is to print n - pyramid using * 
n = int(input())
for stars in range(1, n + 1, 2):
    if n<=0 or n%2==0:
        break
    else:
        print("*" * stars)

#Create a function names transpose that receives one argument:
# A list that contains lists. and returns a modified list.
def transpose(lst):
    if len(lst)==0:
        return lst
    modified_list = []
    row_length = len(lst[0])
    col_length = len(lst)
    for i in range(row_length):
        updated_rows = []
        for j in range(col_length):
            updated_rows.append(lst[j][i])
        modified_list.append(updated_rows)
    return modified_list
      
