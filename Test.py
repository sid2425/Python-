#Numbers 
# x=5
# print(type(x)) it returns <class 'int'>

#Floats 
# x=5.5
# y=5.5
# print(x+y)


# String Indexing 

# mystring='abcdefghijk'
# print(mystring)

# Reverse Indexing
# mystring='abcdefghijk'
# print(mystring[-2])

#Slicing
# mystring='abcdefghijk'
# print(mystring[::0]) ValueError: slice step cannot be zero

# mystring='abcdefghijklmnopqrstuvwxyz'
# print(len(mystring))

#Various Method's of str:
# x='Hello Siddarth'
# print(x)

# x='Hello Siddarth'
# print(x+'!')

# x='Mr.Srinivasa Mani '
# print(x.capitalize())->Returns Upper Case of First Letter
# print(x.lower())->Returns in lower Case
# print(x.upper()) -> Returns in Upper Case
# print(x.split())->Spilts the character according whitespaces or divides them into list

#->Indicates Single Line Comments

#.format() with strings 
# x='Siddarth'
# print("Hello {1} {0}".format("Rakul","Baby")) returns "Hello Baby Rakul"
# print("Hello {x} This is {y}, I {z} big of you".format(x='Rakul',y='Siddarth',z='am'))-> print's Hello Rakul This is Siddarth, I am big of you
# print(f"Hello This is {x}")
# print(f"Hello This is {'Siddartha, Rakul how r u??'}")
result=100/77
print("Hence the result is {r:1.2f}".format(r=result))