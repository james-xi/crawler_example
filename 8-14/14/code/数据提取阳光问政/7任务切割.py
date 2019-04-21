
mylist=[x  for  x in range(103)]
print mylist
xclist=[[],[],[],[],[],[],[],[],[],[]]
N=len(xclist)
for   i  in range(len(mylist)):
    xclist[i%N].append(mylist[i])#求模切割
for  list  in xclist:
    print list