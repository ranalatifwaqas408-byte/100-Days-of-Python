num=int(input("Enter a number:"))
guess=0
while guess*guess==num:
    guess+=1
    if guess*guess==num:
        print(num,"is a perfect square")
    else:
        print(num,"num is not a perfect square")