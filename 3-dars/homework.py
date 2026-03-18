# 1-masala
# day=int(input("Kunni kiriting: "))
# month=int(input("Oyni kiriting: "))
# if day>31 or day<0 or month>12 or month<0:
#     print("Xato")
#     exit(0)
# day+=1
# if month in [1,3,5,7,8,10,12]:
#     max_kun=31
# elif month in [4,6,9,11]:
#     max_kun=30
# else:
#     max_kun=28
# if day>max_kun:
#     day=1
#     month+=1
# if month>12:
#     month=1
#     day+=1
# print(f"{day}-kun {month}-oy")

# 2-masala
# d=int(input("Kunni kiriting: "))
# m=int(input("Oyni kiriting: "))
# if d>31 or d<0 or m>12 or m<0:
#     print("Xato")
#     exit(0)
# d-=1
# if d<=0:
#     m-=1
#     if m==0:
#         m=12
# if m in [1,3,5,7,8,10,12]:
#     d=31
# elif m in [4,6,9,11]:
#     d=30
# else :
#     d=28
# print(f"{d}-kun {m}-oy")


# 3-masala

# son=int(input("Uch xonali son kiriting: "))
# yuz=son//100
# on=son//10%10
# bir=son%10
# if yuz == 1: print("bir yuz", end=" ")
# if yuz == 2: print("ikki yuz", end=" ")
# if yuz == 3: print("uch yuz", end=" ")
# if yuz == 4: print("to'rt yuz", end=" ")
# if yuz == 5: print("besh yuz", end=" ")
# if yuz == 6: print("olti yuz", end=" ")
# if yuz == 7: print("yetti yuz", end=" ")
# if yuz == 8: print("sakkiz yuz", end=" ")
# if yuz == 9: print("to'qqiz yuz", end=" ")

# # onlik
# if on == 1: print("o'n", end=" ")
# if on == 2: print("yigirma", end=" ")
# if on == 3: print("o'ttiz", end=" ")
# if on == 4: print("qirq", end=" ")
# if on == 5: print("ellik", end=" ")
# if on == 6: print("oltmish", end=" ")
# if on == 7: print("yetmish", end=" ")
# if on == 8: print("sakson", end=" ")
# if on == 9: print("to'qson", end=" ")

# # birlik
# if bir == 1: print("bir")
# if bir == 2: print("ikki")
# if bir == 3: print("uch")
# if bir == 4: print("to'rt")
# if bir == 5: print("besh")
# if bir == 6: print("olti")
# if bir == 7: print("yetti")
# if bir == 8: print("sakkiz")
# if bir == 9: print("to'qqiz")


# 4-masala
# son=int(input("Son kiriting: "))
# sum=0
# temp=son
# while temp!=0:
#     r=temp%10
#     sum+=r
#     temp//=10
# print((son%sum)

# 5-masala
# a=int(input("1-sonni kiriting: "))
# b=int(input("2-sonni kiriting: "))
# sum=0
# for i in range(a,b+1):
#     sum+=i
# print(f"Yig'indi: {sum} ga teng")

# 7-masala
# a=int(input("Sonni kiriting: "))
# faktorial=1
# for i in range(1,a+1):
#     faktorial=faktorial*i
# print(faktorial)

# 8-masala
# a=int(input("Sonni kiriting: "))
# c=0
# temp=a
# while a%2==0:
#     a=a//2
#     c+=1
# print(f"{temp} 2 ga {c} marta bo'linadi")

# 9-masala
# son=int(input("Sonni kiriting: "))
# for i in range(son,son*2+1):
#     print(i)

# 10-masala
# a=int(input("Boshlang'ich sonni kiriting: "))
# b=int(input("Oxirigi sonni kiriting: "))
# for i in range(a,b+1):
#     c=0
#     for j in range(2,i):
#         if i%j==0:
#             c+=1
#     if c==0 :
#         print(i)

# 11-masala
# a=int(input())
# for i in range(1,a):
#     if a%i==0:
#        if i%2==1:
#            print(i)
# 12-masala
# a=int(input())
# c=0
# for i in range(1,a):
#     if a%i==0:
#         c+=i
# print(c)

# 13-masala

# a=int(input("Boshlang'ich sonni kiriting: "))
# b=int(input("Oxirgi sonni kiriting: "))
# sum=0
# for i in range (a,b):
#     c=0
#     for j in range (2,i):
#         if i%j==0:
#             c+=1
#     if c==0 and i>1:
#         sum+=i
# print(f"Tub sonlar yig'indisi: {sum} ga teng")

# 14-masala

for i in range (5,0):
    for j in range (i-1,0):
        print("*", end=" ")
    print("\n")


      







