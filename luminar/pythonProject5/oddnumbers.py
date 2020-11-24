low=int(input("enter lower numbers"))
upp=int(input("enter upper numbers"))
sum=0
if(low>upper):
    print('error')
while(i<=upper):
    if(low%2!=0):
        low+=1
        print(sum)