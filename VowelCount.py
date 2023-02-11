s = input().lower()
vowel = ('a', 'e', 'i', 'o', 'u', 'A','E','I','O','U')
count = 0
for index, i in enumerate(s[1:]):
    if i not in vowel and s[index] in vowel:
        count += 1
print(count)