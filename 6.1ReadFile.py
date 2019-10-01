# Using the names.txt file you've downloaded:
# read file
# count lines in files
# close files


def main():
    # Open a file titled names.txt
    infile = open('names.txt', 'r')

    # Read the file's contents
    file_contents = infile.read()

    while file_contents != "":
        print(file_contents)
        file_contents = infile.read()

    # Close the file
    infile.close()


# Call the main function
main()

"""
    record = input_filereadline()
    input_file.close()
"""
