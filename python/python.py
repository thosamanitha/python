# radius=4
# pi=3.14
# perimeter=2*pi*radius
# print(perimeter)
# area=pi*(radius**2)
# print(area)

# age=float(input())
# if 12<age<18:
#     g_s="teen"
#     print("g_s: " +g_s)
    
# elif 18<=age<21:
#     print("Growth Stage:Young Adult")
# elif 18>=21:
#     print("Growth Stage:Adult")
# elif age<=12:
#     print("Growth Stage:child")
  
# print(str(age) + " Years old")



# n=int(input())
# i=1
# while i<n:
#     print(end=" " + str(i))
#     i=i+1
    

# n,i=int(input()),1
# output="1"
# while i<n:
#     i+=1
#     if i%5==0:
#         continue
#     output+= " " + str(i)
# print (output)



# def add(a,b):
#     return a+b
# print(add(b="anu",a="chinni")) #keyword arguments
# print(add("anu","chinni")) #positional arguments


# def add(a,b):
#     return a+b
# print(add(a=2,b=3))



# def add(a,b):
#     return a+b

# def multiply(a,b):
#     return a*b

# def operate(a,b,operation=add):
#     return operation(a,b)
# print (operate(2,4))
# print (operate(2,4,operation=multiply))



# def get_operator(operator):
#     if operator=="ADD":
#         return add
#     elif operator=="MULTIPLY":
#         return multiply
# op=get_operator("ADD")
# op(2,4)
# op=get_operator("MULTIPLY")
# op(2,4)



add=lambda x,y:x+y
print(add(1,2))