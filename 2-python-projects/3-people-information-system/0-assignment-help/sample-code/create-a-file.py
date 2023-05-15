id = input("Enter ID: ")


f = open(f"{'sample.txt'}", "w")
f.write("Woops! I have deleted the content!")
f.close()