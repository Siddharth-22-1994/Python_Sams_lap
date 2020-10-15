str1 = input()
str2 = input()

sort_str1 = sorted(str1)
sort_str2 = sorted(str2)

if (sort_str1 == sort_str2):
    print("The given strins are Anagram")
else:
    print("The given string are not Anagram")
    
