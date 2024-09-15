"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

with open("src/foo.txt") as f:
    newFile = f.read()

print(newFile)

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

newFile = open("src/bar.txt", "w")

newFile.write("Sampson: If you do, sir, I am for you: I serve as good a man as you.\n")
newFile.write("Abraham: No better.\n")
newFile.write("Sampson: Well, sir.\n")
newFile.write("Gregory: (to Sampson) Say 'better'; here comes one of my master's kinsmen.\n")
newFile.write("Sampson: Yes, better, sir.\n")
newFile.write("Abraham: You lie.\n")
newFile.write("Sampson: Draw, if you be men! Gregory, remember thy swashing blow.\n")

newFile.close()

with open("src/bar.txt") as f:
    read_data = f.read()

print(read_data)
