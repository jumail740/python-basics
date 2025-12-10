############   DATA TYPES   ##################                    

# a=10
# print(a)
# print(type(a))

# b=10.0
# print(b)
# print(type(b))

# c= "hello"
# print(c)
# print(type(c))

# d= True
# print(d)
# print(type(d))

# e= [1,2,3]
# print(e)
# print(type(e))

# f=(1,2,3,4,5)
# print(f)
# print(type(f))

# g={1,2,3}
# print(g)
# print(type(g))

# h={'name':"jumail"}
# print(type(h))


########OPERATORS#######################

# Arithmetic Operators

# a=10
# b=20
# print(a+b)  
# print(a-b)
# print(a*b)  
# print(a/b)
# print(a%b
# print(a//b) 
# print(a**b)

#Assignment operators

# a=10
# print(a)
# a+=1
# print(a)
# a-=1
# print(a)
# a*=2
# print(a)
# a/=2
# print(a)

# Relational Operators

# a=10
# b=20
# print(a==b)
# print(a<=b)
# print(a>=b)
# print(a<b)
# print(a>b)
# print(a!=b)

# Logical operator


# a=20
# b=20
# print(a==b and a<b)
# print(a==b or a!=b)
# print(not(a<b))
 
# identity operator

# is, is not 

# a=20
# b=20
# print(a is b)
# print(a is not b)

# Membership Operators

# in ,not in 

# a="hello"
# print("j" in a)
# print("j" not in a)
# print("e" in a)
# print("e" not in a)
# a=["hii","hloo","hoo"]
# print("j" in a)
# print("hii" in a)

# Conditional statements 

# if 

# a=10
# if(a>20):
#     print(a,"a is less than 20")
# # else if
# a=10
# if(a>20):
#     print(a,"a is greater than 20")
# else:
#     print(a,"is less than 20")

# odd or even 

# a=10
# if a%2==0:
#     print(a ,"is even")
# else:
#     print(a ,"is odd")


# elif

# day=int(input("enter a number corresponding to a days:"))
# if day==1:
#     print("Sunday")
# elif day==2:
#     print("Monday")
# elif day==3:
#     print("Tuesday")
# elif day==4:
#     print("Wednesday")
# elif day==5:
#     print("Thursday")
# elif day==6:
#     print("Friday")
# elif day==7:
#     print("Saturday")
# else:
#     print("invalid day")

# Nested if

# a=int(input("enter the first number:"))
# b=int(input("enter the Second number:"))
# c=int(input("enter the Third number:"))

# if a>b:
#     if a>c:
#         print(a," a is larger")
#     else:
#         print(c, "c is larger")
# else:
#     if b>c:
#         print(b,"b is larger")
#     else:
#         print(c,"c is larger")


# Loops

# For Loop

    # increment
# for i in range(1,11):
#     print(i)

    # decrement
# for i in range(10,0,-1):
#     print(i)

    # even number
# for i in range(1,11):
#     if i%2==0:
#      print(i)
    
# a=int(input("enter a number"))
# b=int(input("enter a number"))

# for i in range(a,b+1):
#      print(i)

    # sum
# sum=0
# for i in range(1,11):
#     sum+=i
    
# print(sum)


                        # while loop 

    #   increment

# i=0
# while(i<=10):
#     print(i)
#     i+=1

     # decrement 

# i=10
# while(i>=0):
#     print(i)
#     i-=1

#   even   

# i=0
# while(i<=10):
#      i+=1
#      if(i%2==0):
#         print(i)

    #    input

# a=int(input("enter a number:"))
# b=int(input("enter a number:"))
# i=0
# while(a<=b):
#     print(a)
#     a+=1
    #   sum

 # sum=0
 # i=0
 # while(i<10):
 #     i+=1
 #     sum+=i
     
# print(sum)

# i=0
# while(i<10):
#     i+=1
#     if i!=6:
#         print(i)
        
# for i in range(1,10):
#     print(i,end=" ")

    
# star print 

# for i in range(3):
#     for j in range(4):
#         print("*" ,end='')
#     print()

# 111
# 222
# 333

#  for i in range(1,4):
#     for j in range(3):
#         print(i,end=" ")
        
#     print() 
    
    #123
    # 123
    # 123 
    
# for i in range(3):
#     for j in range(1,4):
#         print(j,end=" ")
        
#     print() 
    
# 123
# 456
# 789

# num=1
# for i in range(3):
#     for j in range(3):
#         print(num,end=" ")
#         num+=1
#     print()

# 123
# 234
# 345

# for i in range(1,4):
#     for j in range(3):
#         print(i,end=" ")
#         i+=1
#     print()
    

# for i in range(1,4):
#     num=i
#     for j in range(3):
#         print(num,end=" ")
#         num+=1
#     print()


# *
# * *
# * * *
# * * * *
# * * * * *
# * * * * * *


# for i in range(6):
#     for j in range(i):
#         print("*",end=" ")
#     print("*")

# A B C 
# D E F 
# G H I
                                                                             
# a=65
# for i in range(3):
#     for j in range(3):
#         print(chr(a),end=" ")
#         a+=1
#     print()