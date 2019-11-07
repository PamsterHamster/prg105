# Write a program that asks the user to enter a 10-character telephone number in the format XXX-XXX-XXXX.
# The application should display the telephone number with any alphabetic characters that appeared in the original
# translated to their numeric equivalent. HINT: Create a variable to hold the converted phone number and
# concatenate one number at a time on to the end of it. Suggestion: Try using Parallel Lists.

# i.e. Please enter the phone number (1-800-get-food) that you want to convert to numbers: 1-800-get-food
# 1-800-438-3663
"""
# LOGIC redo Nov 8, 2019
Main

Data:
    Variables:

           Character_list [‘-‘,‘1’, ‘2’, ‘3’, ‘4’, ‘5’, ‘6’, ‘7’, ‘8’, ‘9’, ‘0’, ‘A’, ‘B’, ‘C’, ‘D’, ‘E’ …]

            Keypad_list.    [‘-‘,‘1’, ‘2’, ‘3’, ‘4’, ‘5’, ‘6’, ‘7’, ‘8’, ‘9’, ‘0’, ‘2’, ‘2’, ‘2’, ‘3’, ‘3’ …]

            user-phone : get phone number from user

Processing:
    Variables:

            phone_out -  will hold numeric phone number

    Loop:

        for character in user_phone
                        Check if an alpha character
                                    If it is convert it to an upper case
                                    Get the index of it in the character list
                                    Concatenate the character at the same index from the character list to
                                        the phone_out variable

Output:

            Print the phone_out variable with a friendly message
"""


def main():
    # data
    character_list = ['-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
                      'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    keypad_list = ['-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '2', '2', '2', '3', '3', '3', '4', '4',
                   '4', '5', '5', '5', '6', '6', '6', '7', '7', '7', '7', '8', '8', '8', '9', '9', '9', '9']

    user_phone = input("Please enter the phone number to be converted (1-800-Get-Food): ")

    # processing
    phone_out = ""
    for number in user_phone:
        if number.isalpha():
            number = number.upper()
        my_index = character_list.index(number)
        phone_out = phone_out + keypad_list[my_index]


# output
    print("The numeric value of your phone number is: ", phone_out)


main()

"""
def main():
    alpha = ['0', '1', '2', 'A', 'B', 'C', '3', 'D', 'E', 'F', '4', 'G', 'H', 'I', '5', 'J', 'K', 'L', '6', 'M', 'N',
         'O', '7', 'P', 'Q', 'R', 'S', '8', 'T', 'U', 'V', '9', 'W', 'X', 'Y', 'Z', '-']

    digits = ['0', '1', '2', '2', '2', '2', '3', '3', '3', '3', '4', '4', '4', '4', '5', '5', '5', '5',
          '6', '6', '6', '6', '7', '7', '7', '7', '7', '8', '8', '8', '8', '9', '9', '9', '9', '9', '-']

    phrase = input('Please enter a ten-digit phone number to translate into numbers: ')

    # print(len(phrase))
    tele_final = ""
    for letter in phrase:
        for item in range(0, len(standard)):
            if letter.upper() == standard[item]:
                tele_final += (alpha[item] + " ")

main()

# try one BUT I think it's backwards...?
pho_number = input('Please enter a ten-digit phone number : ')


def area_code = num[0]
    numend = num[1:]
    number = ''
    for n in numend:
        for i in range(len(n)):
            if n[i] in 'ABC':
                number = number + '2'
            elif n[i] in 'DEF':
                number = number + '3'
            elif n[i] in 'GHI':
                number = number + '4'
            elif n[i] in 'JKL':
                number = number + '5'
            elif n[i] in 'MNO':
                number = number + '6'
            elif n[i] in 'PQRS':
                number = number + '7'
            elif n[i] in 'TUV':
                number = number + '8'
            elif n[i] in 'WXY':
                number = number + '9'
        number = number + '-'
    return area_code + '-' + number[:-1]

    pho_number = '555-GET-FOOD'
    newalpha_num = pho_number
    print()
    phnum(pho_number):
        num = phnumber.split('-')
    
"""
