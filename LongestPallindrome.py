# # def solve(A,B):
# #     arr=[]
# #     for i in range(len(B)):
# #         index=B[i]
# #         if (A[index-1]==A[index+1]):
# #             print("True")
# #             arr.append(index-1)
# #             arr.append(index+1)
# #         print("fasle")
# #         print(arr)



# # A="aaaaa"
# # B=[2,3]
# # solve(A,B)
# def longestPalSubstr(string):
#     n = len(string) # calculating size of string
#     if (n < 2):
#         return n # if string is empty then size will be 0.
#                   # if n==1 then, answer will be 1(single
#                   # character will always palindrome)
#     start=0
#     maxLength = 1 
#     for i in range(n):
#         low = i - 1
#         high = i + 1
#         while (high < n and string[high] == string[i] ):                               
#             high=high+1
        
#         while (low >= 0 and string[low] == string[i] ):                 
#             low=low-1
        
#         while (low >= 0 and high < n and string[low] == string[high] ):
#           low=low-1
#           high=high+1 
          
      
#         length = high - low - 1
#         if (maxLength < length):
#             maxLength = length
#             start=low+1
              
#     print ("Longest palindrome substring is:",end=" ")
#     print (string[start:start + maxLength])
      
#     return maxLength
      
# # Driver program to test above functions
# string = ("forgeeksskeegfor")
# print("Length is: " + str(longestPalSubstr(string)))

class Solution(object):
   def longestPalindrome(self, s):
      dp = [[False for i in range(len(s))] for i in range(len(s))]
      for i in range(len(s)):
         dp[i][i] = True
      max_length = 1
      start = 0
      for l in range(2,len(s)+1):
         for i in range(len(s)-l+1):
            end = i+l
            if l==2:
               if s[i] == s[end-1]:
                  dp[i][end-1]=True
                  max_length = l
                  start = i
            else:
               if s[i] == s[end-1] and dp[i+1][end-2]:
                  dp[i][end-1]=True
                  max_length = l
                  start = i
      return s[start:start+max_length]
ob1 = Solution()
print(ob1.longestPalindrome("aaaaa"))