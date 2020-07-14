"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

f = open('foo.txt', 'r')
read_data = f.read()
print(read_data)
f.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

f = open('bar.txt', 'w')
write_data = f.write('O! what a silly oaf I am!\n Walked into a bar sauced on suds from the wrong side of town.\n Next I knew, I was hanging by the rafters singing songs upside down!')
f.close()
