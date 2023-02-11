def findPair(A, target):
    for i in range(len(A) - 1):
        for j in range(i + 1, len(A)):
            if A[i] + A[j] == target:
                a=A.index(A[i])+1
                b=A.index(A[j])+1
                print(a,b)
                return 
 
N,sum=map(int, input().split())
arr=list(map(int, input().split()))[:N]
findPair(arr,sum)