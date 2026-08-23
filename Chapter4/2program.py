a = ["Parv","mango",15,20.5,8]
print(a)
a.append("Hola!") #Adds an new element in the end 
print(a)

b = [3,7,4,1,3,4,10]
b.sort()
print(b)

b.reverse()
print(b)

b.insert(3,33) #Here we can insert in any index value instead of end (3,33) first value is index number and second one is the value which we need to insert
print(b)

b[1:1] = [10,20,50] #it insert the values at the index 1 means it starts from 1 then add after that does not replace existing one
print(b)

b[1:3] = [11,22,33,44,55,66] #Here it will replace existing values also if it exceeds limit it will keep on adding elemnts after last value [1,2,3,4,5]
print(b)

b.pop(1) #Pops the index number
print(b.pop(1)) #prints the value at the index
print(b)

b.remove(3)#Does not take index takes the actual values
print(b)