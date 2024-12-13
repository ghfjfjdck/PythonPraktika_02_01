
#___________________
#ZADANIE 1

# a = [1, 1, 2, 3, 5, 8, 10, 12, 34, 38, 40, 41, 46, 50, 55, 89]
# result =[]
# for i in a :
#   if(i<15):
#       result.append(i)
  
# print(result)

#___________________
# Zadanie 2
# print("Enter number")
# number = float(input())
# if(number<0):
#     print("Chislo otricatelnoe")
# else:
#     if(number>0):
#         print("Chislo pologitelnoe")
#     else:
#         print("Chislo = 0")

#_____________
# ZADANIE 3
# print("Enter first number")
# num1 = float(input())
# print("Enter second number")
# num2 = float(input())
# print("Enter +,-,/,*")
# result=0
# symbol = (input())
# if( symbol =='+'):
#         result = num1+num2
# else:
#         if(symbol=='-'):
#             result=num1-num2
#         else:
#             if(symbol=='/'):
#                 result = num1/num2
#             else:
#                 if(symbol=='*'):
#                     result=num1*num2
#                 else: 
#                     print("Error")
                    
# print(result)

#_________________
# ZADANIE 4
# i=10
# while i!=0:
#     print(i)
#     i=  i-1

#____________________
#ZADANIE 5
# import math
# a = float(input("Enter a: "))
# b = float(input("Enter b: "))
# c = float(input("Enter c: "))

# if a == 0:
#     print("This is not a quadratic equation")
# else:
#     discr = b**2 - 4*a*c
#     if discr >= 0:
#         x1 = (-b - math.sqrt(discr)) / (2*a)
#         x2 = (-b + math.sqrt(discr)) / (2*a)
#         print("x1 =", round(x1,2))
#         print("x2 =", round(x2,2))
#     else:
#         print("The discriminant is less than zero, the roots are complex.")