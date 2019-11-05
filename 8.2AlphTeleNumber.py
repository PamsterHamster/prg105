# Write a program that asks the user to enter a 10-character telephone number in the format XXX-XXX-XXXX.
# The application should display the telephone number with any alphabetic characters that appeared in the original
# translated to their numeric equivalent. HINT: Create a variable to hold the converted phone number and
# concatenate one number at a time on to the end of it. Suggestion: Try using Parallel Lists.

# i.e. Please enter the phone number (1-800-get-food) that you want to convert to numbers: 1-800-get-food
# 1-800-438-3663

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





"""
# try one BUT I think it's backwards...?
pho_number = input('Please enter a ten-digit phone number : ')


def phnum(pho_number):
    num = phnumber.split('-')
    area_code = num[0]
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
"""
