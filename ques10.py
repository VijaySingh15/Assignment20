def check(s1,s2):
    if(sorted(s1)==sorted(s2)):
        print("This is anagram")
    else:
        print("This is not anagram")

s1=input("Enter word :")
s2=input("Enter another word :")
check(s1,s2)