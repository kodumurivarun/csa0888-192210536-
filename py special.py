s=input()
count=0
set1=set(s)
set1.discard(' ')
list1=list(set1)
for i in list1:
    if not i.isalpha():
        if not i.isdigit():
            count+=1
print(count)

