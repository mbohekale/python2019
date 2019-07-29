##fibonacci is the sequence of natural number and sum of the previous two is call
##fibonacci
##a,b,c,d,e,f,g,h
##c = a+b
##d =c+b

def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
for i in range(1,12):
    print(fib(i))
    

