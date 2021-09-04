#arr=[3,3,-1,2,-1,4,5,-1,-1,9,8]
a=[3,3,-1,2,-1,4,5,-1,-1,9,8]
suy=[]
kp=[]
#c=0
for i in a:
    if i == -1:
        kp.append(i)
    else:
        suy.append(i)
print(suy+kp)
