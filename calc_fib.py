def recurssive_fib(input):
    if input is 0:
        return 0
    elif input is 1:
        return 1
    else:
        return recurssive_fib(input-1) + recurssive_fib(input-2)

def fib(input):
    if input is 0:
        return 0
    elif input is 1:
        return 1
    else:
        fiblist = [0,1]
        for i in range (2, input+1):
            fiblist.append(fiblist[i-2] + fiblist[i-1])
        return fiblist[-1]



#print(recurssive_fib(25))
print(fib(40))


