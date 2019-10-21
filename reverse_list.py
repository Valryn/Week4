def reverse(inputlist):
    if len(inputlist) <= 1:
        return inputlist
    else:
        temp = [inputlist[-1]]
        return temp + reverse(inputlist[:-1])


mylist = [1, 2, 3, 4, 5]

print(reverse(mylist))
print(mylist)