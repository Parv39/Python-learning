a = ["Parv","Hello","Pineapple","pink"]
for name in a:
    if(name.lower().startswith("p")):
        print(f"Hello{name}")
    else:
        print("Not Found")