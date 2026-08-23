a = (1,4,5,6,7,10) #This is tuple denoted by () immutable cannot change data 
b = ()#Empty tuple
c = (1,)#Tuple with only 1 value as c=(1) will be int
print(type(b))
print(type(a))
print(type(c))

a1 = (1,5,7,2,"Parv",True,5)
print(a1)
print(a1.count(5)) #Used to count the given element in tuple
print(a1.index("Parv")) #To find index of value