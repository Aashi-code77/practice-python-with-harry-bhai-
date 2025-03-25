# problem 1 :-  write a python program to add two numbers.
a = 1 
b = 2
print(a+b)

# problem 2 :- write a python program to find remainder when a number is divided by Z
a = 37
b = 5 
# print( a % b) # aise bhi kr sakte h 
print("Remainder when a is divided by b is ", a % b)

# problem 3 :-  check the type of variable assigned using input() function.
a = input("Enter the value of a: ") # input ka type  <class 'str'> 
print(type(a))

#  problem 4 :-  use comparison operator to find out whether a given variable a is greater than 'b' or not. take a = 34 and b = 80
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
print ("a is greater than b is ", a>b)

#  problem 5 :-  write a python program to find an average of two numbers entered by the user.
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
print("The average of these two number is",(a+b)/2)

#  problem 6 :- write a python program to calculate the square of a number entered by the user.
a = int(input("Enter your number : "))
print("The square of the number is",(a**2))
print("The cube of the number is",(a**3)) # a**n -- we find the number of n multiple
# print("The square of the number is",(a*a)) # its also a right way to find square of the number
# print("The square of the number is " , a^2)  # Incorrect for finding square of a number in python