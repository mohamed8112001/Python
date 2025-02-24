# program 1

# print("hello")
# count = 0
# str = input('Enter the name:')
# chars=['a','e','i','o','u']
# for c in chars:
#     for ch in str:  
#         if( c == ch ):
#             count=count+1
# print(f" the number of vowels in {str} : {count}")

#program 2

# def fun1(length,start):
#     numbers=[]
#     num=0
#     while num<length:
#         numbers.append(start+num)
#         num+=1
#     print(numbers)


# fun1(10,5)




# program 3

# numbers=[]
# num = 0
# while num<5:
#     elm = input(f"enter the elm {num} : ")
#     numbers.append(int(elm))
#     num+=1

# print(numbers)
# numbers.sort(reverse=True) 
# print(numbers)   

# numbers.sort(reverse=False) 
# print(numbers)

# program 4

# def fun():
#     num = int(input("enter the number : "))

#     if ( num%3==0 and num%5==0 ):
#         print("FizzBuzz")
#     elif (num%5==0):
#         print("Buzz")
#     elif(num%3==0):
#         print("Fizz")
        
# fun()


# proplem 5

# def fun():
#     str = input("enter the name : ")
#     str1 = str[::-1]
#     print(str)
#     print(str1)


# fun()


# proplem 6
# import math

# def fun():
#     radius = int(input("enter the radius : "))
#     area = math.pi * math.pow(radius,2)
#     area = math.pi * (radius ** 2)
#     Circumference = math.pi * 2 * radius

#     print(f"Area of circle : {area}")
#     print(f"Circumference of circle : {Circumference}")

# fun()

# program 7

# def fun():
#     name = input("enter your name: ")
#     if name.isalpha:
#         # name.isdigit() name.isalpha or name.strip() =="":
#         print("not falid")
       
#     email = input("enter your email: ")

#     print("Info For User : ")
#     print(f"name of user :{name}")
#     print(f"email of user :{email}")

# fun()      


# program 8

# str = "iti ,lam in iti "

# print(str.count("iti") )




# tuple use to store collection of immutable elements
# diffferent datatype
# #Packing ==> set more values in one variable(list or tuple)
# mixed = (1,'mohamed',True,3.14)
# # datatype => tuple => the element store in ()
# print(type(mixed))

# print(mixed)
# for item in mixed:
#     print(item)

# print(mixed[0])
# mixed[0] = 10 => error because tuple not modifie

# mixed_list = list(mixed)
# print(mixed_list)
# # datatype => list => and the data store in [] 
# print(type(mixed_list))
# print(mixed_list[1])
# # can modifie any item of list 
# mixed_list[1]="mustafa" 
# print(mixed_list[1])


# # UnPacking ==> export the value from list or tuple and set in more variable
# # set the value from tuple or list
# person=["mohamed","mustafa",23]
# f_name,l_name,age=person

# print(f_name)
# print(l_name)
# print(age)


