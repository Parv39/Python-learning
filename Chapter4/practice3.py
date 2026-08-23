a = (10,15,"Parv")

a[1] = 5 #Tupple cannot be changed

t = (10, 20, 30)

l = list(t)      # Convert tuple to list
l[1] = 50        # Change the value
t = tuple(l)     # Convert back to tuple

print(t)