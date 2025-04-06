#1 write a program to create a dictionary of hindi words with values as their English translation. provide user with an option to look it up!
words = {
    "madad": "Help",
    "kursi": "chair",
    "billi": "Cat"
}
word = input("Enter the word you want meaning of: ")
print(words[word])


#2 write a program to input eight numbers from the user and display all the unique numbers(once).
s = set()
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
print(s)


#3 Can we have a set with 18 (int) and '18'(str) as a value in it ?
s = set()
s.add(18)
s.add("18")
print(s)
# yes 


#4 what will be the length of following set s:
s = set()
s.add(20)
s.add(20.0)
s.add('20')
print(s) # length of s : 2
# because  in python  '1 == 1.0 ' evaluates to 'true' 


#5 what is the type of 's' in s = {}
s={} 
print(type(s))   # <class 'dict'>  


#6 create an empty dictionary.Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.
d = {}
name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

print(d)


#7 if the names of 2 friends are some ; what will happen to the program in problem 6?
#  key same nhi ho sakta isliye the values entered later will be updated
 

#8 if languages of two friends are same ; what will happen to the program in problem 6?
#  nothing will happen. The values can be same



#9 can you change the values inside a list which is contained in set S? 
# S = {8,7,12,"harry",[1,2]}

# No, you cannot change the values inside the list [1,2] because a set in Python can only contain immutable (unchangeable) elements. 
# A list is mutable, so Python will raise an error when you try to include it inside a set.

# Why?

# Sets require all elements to be hashable
# Lists are not hashable because they can be changed (mutable).
# This means Python will raise a TypeError when you try to create S.









