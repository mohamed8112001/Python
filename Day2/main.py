#program 1

# str = input("enter string: ")
# print(str)

# list=[]
# i=0
# for c in str :
#     # i=0 
#     if c == 'i':
#         list.append(i)
#     i=i+1

# print(list)        

str = input("enter string:")
list=[]
for i,name in enumerate(str):
    if name == 'i':
        list.append(i)
print(list)        

# program 2

# # num = int(input("enter num of table: "))
# list1=[]
# # n=1
# for n in range(1,num+1):
#     # init=1
#     list=[]
#     # print(f"parent{n}")
#     for init in range(1,n+1):
#     #     print("===")
        
#         # print(f"child{init}")
#         # print(init*n)
#         list.append(init*n)
#         # list.append(init*n)
#         # if(init == n):
#     list1.append(list)
#     # init+=1
# # n+=1

# # print(list1) 
 
# program 3

# names=[]
# list=["ahmed","fatma","ibrahim"]
# l={}
# for name in list:
#     print(name)
#     l[name[0]] = [name]
# print(l)    