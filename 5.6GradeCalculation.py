def calc_average(score1, score2, score3, score4, score5):
    average = (score1 + score2 + score3 + score4 + score5) / 5
    return average


def determine_grade(user_score):
    if user_score < 60:
        return "F"
    elif user_score < 70:
        return "D"
    elif user_score < 80:
        return "C"
    elif user_score < 90:
        return "B"
    elif user_score < 101:
        return "A"


def ask_for_score():
    score1 = float(input(" Please enter score 1: "))
    score2 = float(input(" Please enter score 2: "))
    score3 = float(input(" Please enter score 3: "))
    score4 = float(input(" Please enter score 4: "))
    score5 = float(input(" Please enter score 5: "))

    return score1, score2, score3, score4, score5


def print_tableofresults(score1, score2, score3, score4, score5):
    print("Score\tLetterGrade")
    print(str(score1) + "\t", determine_grade(score1))
    print(str(score2) + "\t", determine_grade(score2))
    print(str(score3) + "\t", determine_grade(score3))
    print(str(score4) + "\t", determine_grade(score4))
    print(str(score5) + "\t", determine_grade(score5))


def main():
    score1, score2, score3, score4, score5 = ask_for_scores():
    print_tableofresults(score1, score2, score3, score4, score5)


main()




# Display
# print()

# Rubric: Write a program that asks a user to enter five test scores. You will need to create five variable to hold
# these scores.
# The purpose of this assignment is to get practice passing information between functions. This is not a good example
# of the way programs are really written, but it will help you understand how to pass parameters.

# Write the Following Functions:
#
# main -
#
# asks the user for each of the five test scores, stores them in separate variables (score1, score2, etc)
# calls calc_average and passes the five variables, storing the result in a variable
# average = calc_average(score1, score2, score....
# calls determine_grade, passing it the average variable, storing the result in a variable
# prints the letter grade
# calc_average -
#
# This function should accept the five test scores as arguments
# returns the average of the scores.
# determine_grade -
#
# This function should accept the average of the test scores as an argument
# returns a letter grade based on the following scale:
#
# Grade Scale
# Score	Letter Grade
# 90-100	A
# 80-89	B
# 70-79	C
# 60-69	D
# Below 60	F
# Hint: determine_grade will use elif
