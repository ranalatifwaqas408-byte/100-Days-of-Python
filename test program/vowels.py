word=input("Enter a word:")
count=0
vowels="aeiouAEIOU"
for letter in word:
    if letter in vowels:
        count+=1
        print("Number of vowels:",count)