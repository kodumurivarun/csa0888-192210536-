a=[[1,2,3,],[2,3,4],[3,4,5]]
rsum=0
csum=0
dsum=0
print(len(a))
for i in range(len(a)):
    for j in range(len(a)):
        rsum+=a[i][j]
    print("the sum of",i,"th row is",rsum)
    rsum=0
for i in range(len(a)):
     for j in range(len(a)):
         csum+=a[j][i]
print("the sum of",i,"th colum is",csum)
for i in range(len(a)):
     for j in range(len(a)):
         if i==j:
             dsum+=a[i][j]
print("the sum of diagonal:",dsum)
             
     
         