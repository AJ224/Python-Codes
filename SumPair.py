def SumPair(arr, n, sum):
    count = 0  # Initialize result
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == sum:
                count += 1
    return count
    
n = int(input())
arr = [int(i) for i in input().split()][:n]
sum = int(input())
print(SumPair(arr, n, sum))