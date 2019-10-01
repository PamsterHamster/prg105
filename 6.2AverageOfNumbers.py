# math from file input
# Calculate the avg of all the numbers stored in the numbers.txt
# THIS IS RESUBMISSION


def main():
    try:
        numbers_file = open('numbers.txt', 'r')
    except IOError as error:
        print("File not found ", error)
    else:
        total = 0
        numberoflines = 0
        line = numbers_file.readline()
        line = line.rstrip('\n')

        while line != "":
            numberoflines += 1
            total += int(line)
            line = numbers_file.readline()

        average = total / numberoflines
        numbers_file.close()
        print("Your average is " + format(average, '.2f'))


main()

"""
    input_file = open('numbers.txt', 'r')


    record = input_file.readline()
    record = record.rstrip('\n')

    while record != "":
        record = int(record)
        if record > 4649:
            high += 1 # IS this correct range the +=1?
        if record < 4:
            low += 1  # IS this correct range?

        record = input_file.readline()
        record = record.rstrip('\n')

    print("There were ", high, " numbers more than _______.")
    print("There were ", low, " numbers less than _______.")

    input_file.close()
"""
