import math

def palindrome(num):
    #return int(num != 0) and ((num % 10) * (10**int(math.log(num, 10))) + palindrome(num // 10))
    return str(num)==str(num[::-1])
    
def solve(A):
    ans = 0
    for i in range(1, A + 1):
        if A % i == 0:
            if i == palindrome(i):
                ans+=1
    return ans


if __name__ == "__main__":
    T = int(input())
    for i in range(1, T + 1):
        A = int(input())
        print("Case #{}:".format(i), solve(A))