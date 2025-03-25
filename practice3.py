# Q1  Write a python program to display a user entered name followed by Good Afternoon using input () function .
name = input("Enter your name: ")
print(f"Good Afternoon, {name} ") # always use f string then use veriable nhi to 2 string ho jayega aur phir error aayega


# Q2  Write a program to fill in a letter template given below with name and date . 
letter = ''' Dear <|Name|>,
            You are selected!
            <|Date|>'''
print(letter.replace("<|Name|>","Harry").replace("<|Date|>", "22 march 2222"))


# Q3 Write a program to detect double space in a string.
name = "Harry is a good  boy and"
print(name.find("  "))  # doble space detecter and find the place of letter in given name just like boy are placed in 16 and placing start with 0 always


# Q4  Replace the double space from problem 3 with single spaces.
name = "Harry is a good  boy and"
print(name.replace("  ", " ")) # this is a function # this replace double space in single space 
print(name) 
 # in this double space remove nhi hua jiska matlab name.replace ka asar name sting  ko print krne pr nhi hoga jaisa name string h vaise hi print hoga  ,name.replace pr new string bnega but vo previous pr koi parbhav nhi dalega
 # jiska SAAF SAAF  matlab h ki string are immutable which means that you cannot change them by running functions on them 


# Q5 Write a program to format the following letter using escape sequence characters. 
letter = "Dear Harry ,\n\tThis python course is nice.\nThanks!"
print(letter)
