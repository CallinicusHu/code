from sys import argv
from os.path import exists
script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

#we could do these two on one line, how?
#in_file = open(from_file)
#indata = in_file.read()
indata = open(from_file).read()

print(f"The input is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTR-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
#in_file.close() kutyád közben lelőtte magát egy légpuskával
