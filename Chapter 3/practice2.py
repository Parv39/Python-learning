l = '''
Dear |name|
You are selected!
|date|
'''
a = input("Enter name:")
b = input("Enter dob:")

print(l.replace("|name|",a).replace("|date|",b))
# First we update an string then again we edited that string to knows as chaining