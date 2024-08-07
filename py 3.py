n=int (input)
digit=""
for i in range (n):
    s= int (input())
    digit+=str(s)
    d=int (digit)
    sum1=0
    while(d!=0):
    a= d%10
    sum1+=a
    d//=10
    print("sum=",sum1)