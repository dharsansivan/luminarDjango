num=int(input("enter number"))
rev=0
while(num!=0)
    digit=num%10
    rev=rev+(digit**3)
    num=num//10
    print(rev)
5