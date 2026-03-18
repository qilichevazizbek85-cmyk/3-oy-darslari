# for i in range(0,100,5):
#     print(i)

# son = 10203
# teskari = 0
# daraja = 1
# while son != 0:
#     if son%10!=0:
#         teskari = teskari + (son % 10)  * daraja # 123
#         daraja *= 10 # 
    
#         son //= 10 # 1
#         print(teskari)

# # 123

# a=2
# b=3
# print((a+b)%2==0)

# harf = "sadf"
# while len(harf) != 1:
#     print("Bitta harf kiriting")
#     harf = input("Harf kiriting: ")


# if harf in "euioa":
#     print("Unli")
# else:
#     print("Unli emas")


son=5
c=0
for i in range (1,son):
    if son%i==0:
        c=c+i
if son==c:
    print("Mukammal")   
else:
    print("Mukammal emas")     