m = {"Parv":89,
     "Priya":55,
     "Riya":87,
     "Manoj":77
}
print(m.items())
print(m.keys())
print(m.values())

m.update({"Parv":98,"Renu":100})
print(m)

print(m.get("Parv")) #If I do Parv1 it gives none
print(m["Parv"]) #This will give error