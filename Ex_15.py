from sys import argv

_, file_path = argv
txt = open(file_path)

print(f"Heres your file {file_path}")
print(txt.read())

print("Type the filename again:")
file_again =  input("> ")
txt_again = open(file_again)
print(txt_again.read())