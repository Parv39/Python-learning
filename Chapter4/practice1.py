a = []
a1 = input("Enter 1 fruit:")
a2 = input("Enter 2 fruit:")
a3 = input("Enter 3 fruit:")
a4 = input("Enter 4 fruit:")
a5 = input("Enter 5 fruit:")
a.append(a1)
a.append(a2)
a.append(a3)
a.append(a4)
a.append(a5)
print(a)

#With loop
n = int(input("How many fruits do you want to enter? "))

fruits = []

for i in range(n):
    fruit = input("Enter fruit: ")
    fruits.append(fruit)

print("Fruits list:", fruits)