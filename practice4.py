#Q1 write a program to store seven  in a list entered by the user .

fruit = []
f1 = (input("Enter fruit name: "))
fruit.append(f1)
f2 = (input("Enter fruit name: "))
fruit.append(f2)
f3 = (input("Enter fruit name: "))
fruit.append(f3)
f4 = (input("Enter fruit name: "))
fruit.append(f4)
f5 = (input("Enter fruit name: "))
fruit.append(f5)
f6 = (input("Enter fruit name: "))
fruit.append(f6)
f7 = (input("Enter fruit name: "))
fruit.append(f7)
print(fruit)


# Q2 write a program to accept marks of 6 students and display them in a sorted manner.

marks= []
f1 = int(input("Enter marks here: "))
marks.append(f1)
f2 = int(input("Enter marks here: "))
marks.append(f2)
f3 = int(input("Enter marks here: "))
marks.append(f3)
f4 = int(input("Enter marks here: "))
marks.append(f4)
f5 = int(input("Enter marks here: "))
marks.append(f5)
f6 = int(input("Enter marks here: "))
marks.append(f6)
marks.sort()
print(marks)

# Q3  check data type cannot be changed in python.
# a=(34,234,"Harry")
# a[2]="Larry"  #  give error -- because tuple are immutable 

#Q4  write a program to sum a list with 4 numbers.  
l = [4,3,5,3]
print(sum(l))   # sum ek function hn

#Q5  write a program to count the number of zeros in the following tuple:
a = (7,0,8,0,0,9)
no = a.count(0)
print(no)

