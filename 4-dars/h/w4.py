# 1-masala
# l=[1, 2, 33, 5, 6, 7, 7]
# a=int(input("sonni kiriting: "))
# for i in range (len(l)):
#     for j in range (i+1,len(l)):
#         if l[i]+l[j]==a:
#             print(i,j)

# 2-masala

# lst = [1, 4, 6, 8]
# for i in range (len(lst)):
#     lst[i]=lst[i]*2
#     print(lst[i], end=" ")

# 3-masala

# lst = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# lst[0]=(10, 20, 100)
# lst[1]=(40, 50, 100)
# lst[2]=(70, 80, 100)
# print(lst)

# 8-masala

satr = "salom2 aziz4 qalaysan3"

# lst.sort()


lst = satr.split(" ")
for i in range(len(lst)-1):
    for j in range (len(lst)-1):
        if int(lst[j][-1]) > int(lst[j+1][-1]):
            lst[j],lst[j+1]=lst[j+1],lst[j]
print(lst)


# print(["A",31][1] > ["B",5][1])










