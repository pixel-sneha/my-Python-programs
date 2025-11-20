def reverse(lst):
    #Write a function named reverse which gets a list of numbers as argument and returns the reversed list.
    revlst = []
    for i in range(len(lst) -1,-1,-1):
        revlst.append(lst[i])
    return(revlst)
