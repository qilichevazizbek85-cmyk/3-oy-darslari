# n= int (input("n= "))
# royxat = []
# for i in range(n):
#     son=int(input(":"))
#     royxat.append(son)
# print(royxat)


# r = [1,2,3,4]
# r.pop(0)
# r.pop()
# r.sort()
# print(r)


# r=[4,2,9,0,12]
# r.sort()
# print(r[1])
# print(r[-2])

r=[]
a=int(input())
while a!=0:
    r.append(a)
    a=int(input())
for i in range(len(r)):
    if r[i]>10:
        r[i]=10
print(r)


l1=[3,1,4]
l2=[1,5,9]
l3=[0,0,0]
l1[0]+l2[0]=l3[0]
l1[1]+l2[1]=l3[1]
l1[2]+l2[2]=l3[2]
print(l3)
    
    



    

