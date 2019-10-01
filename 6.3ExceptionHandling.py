# Imort the 6.2 Average of Numbers assignment. Use try and except statements (I already did this in
# the 6.2 assignment because I'd already started working on 6.3 before submitting and I made a mistake
# in the save/writing of sth...

# Check for both IOE and Value Errors


def main():
    try:
        numbers_file = open('numbers.txt', 'r')
        total = 0.0  # Initialize the accumulator
        numberoflines = 0
        line = numbers_file.readline()

        while line != "":
            numberoflines += 1
            total += int(line)
            line = numbers_file.readline()

        average = total / numberoflines

        numbers_file.close()  # Close the file
    except IOError as err:
        print("An IOError has occured. ", err)
    except ValueError as err:
        print("A value error occured. ", err)
    else:
        print("The average is " + format(average, '.2f'))
    finally:
        print(" You are finished with this program. ")


main()
