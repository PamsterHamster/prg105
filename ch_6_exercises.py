"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free
    Submit your completed file
"""

# TODO 6.1 Introduction to File Input and Output
print("=" * 10, "Section 6.1 file input and output", "=" * 10)
# 1) Assign the variable file_variable to open states.txt in read mode

file_variable = open('states.txt', 'r')

# 2) Close the file
file_variable.close()

# 3) Assign the variable state_capitals to open capitals.txt in write mode.
#    Please note, the file does not currently exist, and by opening it in
#    write mode you will create it

state_capitals = open('capitals.txt', 'w')
state_capitals.write('Springfield')
state_capitals.write('Honolulu')
state_capitals.write('Juneau')

state_capitals.close()

"""
def main():
    outfile = open('state_capitals.txt', 'w')

    # 4) Write three state capitals to the file
    #    There is a list of state capitals here: https://en.wikipedia.org/wiki/List_of_capitals_in_the_United_States
    # Sample:
    #   state_capitals.write("Alabama, Montgomery\n") - make sure to include the \n as a new line symbol

    outfile.write('Illinois, Springfield\n')
    outfile.write('Hawaii, Honolulu\n')
    outfile.write('Alaska, Juneau\n')

    # 5) Close the file
    outfile.close()


main()
"""

# TODO 6.1 reading data in from a file
print("=" * 10, "Section 6.1 reading data from a file", "=" * 10)

# MOST RECENT ATTEMPT DURING OPEN LAB THURS SEP26
states_data = open('states.txt', 'r')
line1 = states_data.readlines()
line2 = states_data.readlines()
line3 = states_data.readlines()

print(line1)
print(line2)
print(line3)

"""
# 1) Assign the variable states_data to open states.txt in read mode
def main():
    infile = open('states_data', 'r')
    # 2) Read in three lines from the file, assign to the variables below, Remove """   """ to test


file_contents = infile.read()
# Prm wont run, doesn't like file_contents variable
line1 = infile.readline()
line2 = infile.readline()
line3 = infile.readline()

# 3) Close the file
infile.close()

# 4) Print the three variables
print(line1)
print(line2)
print(line3)

main()
"""

# TODO 6.2 Using loops to process files
print("=" * 10, "Section 6.2 use loops to process files", "=" * 10)
# Complete the program below to Read in and Count all of the entries in the states file
# Remove the """ """ before testing
# 1) Open the file in read mode using states_file as the file variable
counter = 0

# NEWEST ATTEMPT
states_file = open('states.txt', 'r')
for s in states_file.readlines():
    print(s)
    counter += 1

print(counter)


# MY FIRST ATTEMPT
def main():
    # Open a file states_file
    infile = open('states_file.txt', 'r')

    # Read the file's contents
    infile.read()

    # 2) Write a for loop to read in all of the lines, # STUCK HERE TOO
    # -- print them on the screen,
    # -- and add 1 to counter for each line

    # 3) Close the file
    infile.close()


"""

# TODO 6.3 Processing records
print("=" * 10, "Section 6.3 processing records", "=" * 10)
# You are going to finish the program below to write book information to a file
books = 3  # use this as the number of books to enter

# 1) open the file books.txt for writing, using the variable books_file
# Remove the """ """ to test
books_file = open('books.txt', 'w')  # Used 'a' instead of 'w' because Stephen said 'w' would wipe out re Loop

# 2) Use a for loop to get a title and author from the user using the range 1, books + 1
# -- get the data from the user in the loop
# -- write the data to the file as a record while in the loop,
#    make sure to include the \n at the end of the line

# LATEST ATTEMPT
for b in range(books):
    title = input("Please enter the book title: ")
    author = input("Please enter the book author: ")

    books_file.write(title + " " + author + '\n')

print(books_file.readline())
books_file.close()


"""
"""
#  OK I'm STUCK HERE..same as previous exercise step

# MY FIRST ATTEMPT (working backwards...I thought it might help)
# This is a loop to display a table showing the number of books, title and author
# PRint the table headings for books 1-3 and the headings Title and Author
print('Number\tTitle\tAuthor')
print(----------------------------------)
# Print numbers 1-3
for number in range 1 < 4:
    book1 = number1 + title1 + author1
    book2 = number2 + title2 + author2
    book3 = number3 + title3 + author3
    print(number, '\t', book1)
    print(number, '\t', book2)
    print(number, '\t', book3)

# 3) Close the file

"""

# TODO 6.4 Exceptions
print("=" * 10, "Section 6.4 exceptions", "=" * 10)

# In this exercise you will try to open a file that does not exist,
# capture the error, and display a custom error message

# LATEST ATTEMPT
try:
    file = open('superhero.txt', 'r')

    file.close()
except IOError:
    print("An error occurred trying to read the file, it doesn't exist', superheros.txt")


# MY FIRST ATTEMPT
def main():
    # 1) Create a try statement
    try:
        # 2) Open the file superheros.txt for READING (we are not writing, it would create the file)
        infile = open('superheroes.txt', 'r')
        # 3) Read the contents
        contents = infile.read()
        # 4) Display the file's contents
        print(contents)

        # 3) Close the file
        infile.close()
    # 4) Create an except IOError, that uses a print statement telling the user that the file doesn't exist
    except IOError:
        print('An error occurred trying to read the file: superheros.txt')


main()
