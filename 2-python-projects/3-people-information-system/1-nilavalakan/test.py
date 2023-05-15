id = input("Enter ID: ")


f = open(f"{id}", "w")
f.write(input("Enter your name: ") + "\n")
f.write(input("Enter your age: ") + "\n")



f.close()
