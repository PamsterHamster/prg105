# Variables Age in Years
"""person_age = int
infant <= 1
child >1 and < 13
teenager >= 13 and < 20
adult >= 20 """

# Determine the age classification
person_age = int(input("How old is the person?   "))
if person_age <= 1:
    print("S/he is an infant.")

elif 1 < person_age < 13:
    print("S/he is a child.")

elif 13 >= person_age < 20:
    print("S/he is a teenager.")

else:
    print("S/he is an adult")
