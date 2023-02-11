 
# function to fill Fibonacci
# Numbers in f[]

def fib(f, N):
 

    # 1st and 2nd number of

    # the series are 1 and 1

    f[1] = 1

    f[2] = 1
 

    for i in range(3, N + 1):
 

  
        f[i] = f[i - 1] + f[i - 2]
 
 

def fiboTriangle(n):
    N = n * (n + 1) // 2

    f = [0] * (N + 1)

    fib(f, N)

    fiboNum = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(f[fiboNum], " ", end="")
            fiboNum = fiboNum + 1
        print()
 

n = int(input())
fiboTriangle(n)
 