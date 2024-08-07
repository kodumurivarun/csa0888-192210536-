a=[1,2,4,3]
even=[]
odd=[]
for i in a:
   if i%2==0:
        even.append(i)
else:      
       odd.append(i)
print("odd:",odd)
print("even:",even)
