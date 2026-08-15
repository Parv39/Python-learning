a = int(input("Enter No."))

for i in range(1,a+1):
    print(" "* (a-i), end="") #Using end="" print statement by default does not add new line it's an argument
    print("*"* (2*i-1),end="")
    print("")    