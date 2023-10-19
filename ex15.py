#"""
from sys import argv

scripts, filename = argv

txt = open(filename)
#"""
#x = "krumpli"
#print(x.read())
#"""
print(f"Here's your file {filename}:")
print(txt.read(9))

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
#"""