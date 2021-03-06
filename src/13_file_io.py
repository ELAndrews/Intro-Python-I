"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE

with open('./foo.txt') as f:
    text = f.read()
    print(text)
    # f.close()


# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

with open("./bar.txt", "w") as f:
    f.write("This is my first line. \n Here is another line of arbitrary text \n And this is the final line of random text.")
    # f.close()

with open("./bar.txt", "r") as f:
    text = f.read()
    print(text)
    # f.close()

# When using with => it will close it for you so there is no need to have the close at the end!
