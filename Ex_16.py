from sys import argv

_, file_path = argv

print(f"""
We re going to erase {file_path}
if you dont want that, hit CTRL-C."
if you do want that, hit Enter. 
""")
input("?")

print(f"Opening the file {file_path}")
target =  open(file_path, "w")

print("Trucating the file Goodbye")
target.truncate( )

print("Now Im going to ask you for three lines.")
line1 = input("line 1:")
line2 = input("line 2:")
line3 = input("line 3:")

print("Im goint to write these to the file,")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally we close it.")
target.close()