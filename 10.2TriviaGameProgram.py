import random
import questions


#   INSTRUCTIONS: Creat a simple trivia game for two players. Include the following:
#   Start with player 1. Each player gets a turn at answering 5 trivia questions (total 10 questions).
#   When a question is displayed, 4 possible answers are also displayed. Only one answer is correct.
#   If the player selects correct answer, s/he earns a point.
#   After answers have been selected for all the questions, the program displays the number of points earned
#   by each player and declares the player with highest number points the winner.
#   The program should have an appropriate  __init__method, accessors, and mutators.
#   The program should have a list or dictionary containing 10 Questions Objects, one for each trivia question.
#   Make up your own questions.


def main():
    # My quiz questions

    ques1 = questions.MusicQuiz('Which classical music composer both suffered from TRISKAIDEKAPHOBIA-the fear of the \
                            number 13- AND died on Friday the 13th, 1951?', 'Shostakovich', 'Horowitz', 'Schoenberg',
                                'Jay-Z', 'C')

    ques2 = questions.MusicQuiz('Which classical music composer appeared twice on the cover of TIME magazine?',
                                'Bernstein', 'Strauss', 'Copland', 'Taylor Swift', 'B')

    ques3 = questions.MusicQuiz('Which classical composer wrote an entire symphony while deaf still very popular \
                            today?', 'J.S. Bach', 'Beethoven', 'Schumann', 'Ed Sheeran', 'B')

    ques4 = questions.MusicQuiz('What is a hydraulophone?', 'musical waterfall', 'underwater phone', 'musical \
                            instrument', 'construction vehicle', 'C')

    ques5 = questions.MusicQuiz('What are the best woods used to make a violin/viola/cello/bass?', 'Maple & Spruce',
                                'Maple & Spruce', 'Spruce & Cherry', 'Pine & Balsa', 'A')

    ques6 = questions.MusicQuiz('What is the base starting price for a professional grade violin or viola?', '$500',
                                '$3,000', '$10,000', '$100,000', 'C')

    ques7 = questions.MusicQuiz('The hairs on a violin/viola/cello/bass bow come from which animal?', 'Sheep Dog',
                                'Yak', 'Horse tail/mane', 'Puli Dog', 'C')

    ques8 = questions.MusicQuiz('The part of the violin bow where your right thumb balances is called what?', 'Frog',
                                'Balancer', 'Crotch', 'Angle', 'A')

    ques9 = questions.MusicQuiz('The strings for violins/viola/cello/bass used to be made from what? ', 'Horse hair',
                                'Cat guts', 'Rubber bands', 'Plastic', 'B')
    ques10 = questions.MusicQuiz('How many working parts make up a traditional acoustic piano? ', '7,500', '10,000',
                                 '15,000', '20,000', 'A')


all_questions = (ques1, ques2, ques3, ques4, ques5, ques6, ques7, ques8, ques9, ques10)

print('######PLAYER ONE######')
player1 = input(all_questions)
print('#####PLAYER TWO#####')
player2 = input(all_questions)

# run quiz
if player1 == player2:
    print('No winner. Your scores tied.')
elif player1 > player2:
    print('Congratulations Player One. You are the winner!')
else:
    print('Congratulations Player Two, you are the winner!')

    # Functions


def ask(all_questions):
    correct = 0
    for item in range(2):
        player_questions = random.choice(all_questions)
        print(player_questions.get_question())
        print('A. ' + player_questions.get_answer1())
        print('B. ' + player_questions.get_answer2())
        print('C. ' + player_questions.get_answer3())
        print('D. ' + player_questions.get_answer4())
        player_response = input('Enter the letter of your answer: ')

        if player_response.upper() == player_questions.get_correct_answer():
            print('\nYay! You scored a point.\n\n')
            correct += 1
        else:
            print('Too bad, so sad. That is not correct. Better luck next time.\n\n')

    return correct


main()


class MusicQuiz:

    def __init__(self, ques, ans1, ans2, ans3, ans4, correct):
        self.__question = ques
        self.__possans1 = ans1
        self.__possans2 = ans2
        self.__possans3 = ans3
        self.__possans4 = ans4
        self.__real_ans = correct

    #   Mutators       ref p540/541

    def set_question(self, ques):
        self.__question = ques

    def set_possans1(self, ans1):
        self.__possans1 = ans1

    def set_possans2(self, ans2):
        self.__possans2 = ans2

    def set_possans3(self, ans3):
        self.__possans3 = ans3

    def set_possans4(self, ans4):
        self.__possans4 = ans4

    def set_real_ans(self, correct):
        self.__real_ans = correct

    #   Accessors

    def get_question(self):
        return self.__question

    def get_possans1(self):
        return self.__possans1

    def get_possans2(self):
        return self.__possans2

    def get_possans3(self):
        return self.__possans3

    def get_possans4(self):
        return self.__possans4

    def get_real_ans(self):
        return self.__real_ans


def __str__(self):
    return '\n' + self.__question + '\n' + self.__possans1 + '\n' + self.__possans2 + '\n' + self.__possans3 + \
           '\n' + self.__possans4 + '\n' + self.__real_ans


"""

#   Display output user question/answer selection
def player_question(self):
    print('Your question is: ' + self.__ques + 'Answer choices: ' + \
          '\nA. ' + self.__possans1 + \
          ''\nB.
    ' + self.__possans2 + \
               '\nC.
    ' + self.__possans3 + \
               '\nD.
    ' + self.__possans4) \
    '

    # Run the Music Quiz


def run_quiz(question_objs):
    player1_score = 0
    player2_score = 0

    #### PUT THE GAME CODE HERE...


# Main        See notes from class that day
def Main():
    question_tank = []
    realans_bank = [2, 1, 1, 2, 0. 2, 2, 0, 1, 0]
    for i in range(10):
        ques = 'Question number ' + str(i + 1) + 'here')
        possans1 = 'Choice A: '
        possans2 = 'Choice B: '
        possans3 = 'Choice C: '
        possans4 = 'Choice D: '
        question = Musicquiz(ques, possans1, possans2, possans3, possans4, realans_bank[i])
        question_tank += [question]

        run_Musicquiz(question_tank)

        # Call main

        main()

        # PREVIOUS ATTEMPTS
        #   NOT WORKING/REDO Cite https://www.youtube.com/watch?v=SgQhwtIoQ7o
        question_prompts = {
        "1-Which classical music composer suffered not only from TRISKAIDEKAPHOBIA (the fear of the number 13) 
        but died \n"
        "on Friday the 13th, 1951? \n"
        a) Shostakovich - Russian
        ", \n "
        b) Horowiz - American
        ", \n
        "c) Schoenberg-Austrian",\n
        "2-Which classical composer appeared twice on the cover of TIME magazine?":\n(a)
        Bernstein - American\n(b)
        Strauss\n,
                (c)
        Copland\n\n
        ",
        "3-Which classical composer wrote an entire symphony (still very popular today) while deaf?:\n(a)J.S.Bach\n(b)Beethoven\n
        (c)
        Schumann\n\n
        ",
        "4-What is a hydraulophone?\n(a)musical waterfall\n(b)a phone which works underwater\n(c)a musical instrument:\n
        organ
        powered
        by
        water\n\n
        ",
        "5-What are the best woods used to make a violin/viola/cello/bass?\n(a)Maple & Spruce\n(b)Maple & Oak\n(c)Spruce \n
        & cherry\n\n
        ",
        "6-What is the base starting price for a professional grade violin or viola?\n(a)$500\n(b)$3,000\n(c)$10,000\n\n",
        "7-The hairs on a violin/viola/cello/bass bow come from which animal?\n(a)Sheep Dog\n(b)Yak\n(c)Horse(tail/mane)\n\n",
        "8-The part of the violin bow where your right thumb balances is called what?\n(a)Frog\n(b)Balancer\n(c)Crotch\n\n",
        "9-The strings for violins/viola/cello/bass used to be made from what?\n(a)Horse hair\n(b)Cat gut\n(c)Rubber bands\n\n",
        "10-How many working parts make up a traditional acoustic piano?\n(a)7,500\n(b)10,000\n(c)15,000\n\n"}


        questions = [
            Question(question_prompts[0], "c"),
            Question(question, _prompts[1], "b"),
            Question(question, _prompts[2], "b"),
            Question(question, _prompts[3], "c"),
            Question(question, _prompts[4], "a"),
            Question(question, _prompts[5], "c"),
            Question(question, _prompts[6], "c"),
            Question(question, _prompts[7], "a"),
            Question(question, _prompts[8], "b"),
            Question(question, _prompts[9], "a")]

        def run_test(questions):

            score = 0

        for question in questions:
            answer = input(question.prompt)
            if answer == question.answer:
                score += 1
        print("You got " + str(score) + "/" + str(len(questions)) + "correct.")

    run_test(questions)


      class Question:
          def __init__(self, prompt, answer):
              self.prompt = prompt
              self.answer = answer

class MusicQuiz:

    # the information needed from the data of classes
    def __init__(self, question, possans1, possans2, possans3, possans4, realans):
        self.question = question
        self.possans1 = possans1
        self.possans2 = possans2
        self.possans3 = possans3
        self.possans4 = possans4
        self.realans = realans

    # the formatting for the data information
    def question(self):
        return '{}'.format(self.question)

    def possans1(self):
        return '{}'.format(self.possans1)

    def possans2(self):
        return '{}'.format(self.possans2)

    def possans3(self):
        return '{}'.format(self.possans3)

    def possans4(self):
        return '{}'.format(self.possans4)

    def realans(self):
        return '{}'.format(self.realans)

    #  the specific data


ques1 = MusicQuiz('1.Which classical music composer both suffered from TRISKAIDEKAPHOBIA (the fear of the number 13), \
                  AND died on Friday the 13th, 1951?', 'a-Shostakovich', 'b-Horowitz', 'c-Schoenberg', 'd-Jay-Z')
ques2 = MusicQuiz('2.Which classical music composer appeared twice on the cover of TIME magazine?', 'a-Bernstein',
                  'b-Strauss', 'c-Copland', 'd-Taylor Swift')
ques3 = MusicQuiz('3.Which classical composer wrote an entire symphony (which is still very popular today) while deaf?'
                  'a-J.S. Bach', 'b-Beethoven', 'c-Schumann', 'd-Ed Sheeran')
ques4 = MusicQuiz('4. What is a hydraulophone?', 'a-musical waterfall', 'b-underwater phone', 'c-musical instrument',
                  'd-construction vehicle')
ques5 = MusicQuiz('5.What are the best woods used to make a violin/viola/cello/bass?', 'a-Maple & Spruce',
                  'b-Maple & Spruce', 'c-Spruce & Cherry', 'd-Pine & Balsa')
ques6 = MusicQuiz('6.What is the base starting price for a professional grade violin or viola?', 'a-$500', 'b-$3,000',
                  'c-$10,000', 'd-$100,000')
ques7 = MusicQuiz('7.The hairs on a violin/viola/cello/bass bow come from which animal?', 'a-Sheep Dog', 'b-Yak',
                  'c-Horse tail/mane', 'd-Puli Dog')
ques8 = MusicQuiz('8.The part of the violin bow where your right thumb balances is called what?', 'a-Frog',
                  'b-Balancer', 'c-Crotch', 'd-Angle')
ques9 = MusicQuiz('9.The strings for violins/viola/cello/bass used to be made from what? ', 'a-Horse hair',
                  'b-Cat guts', 'c-Rubber bands', 'd-Plastic')
ques10 = MusicQuiz('10.How many working parts make up a traditional acoustic piano? ', 'a-7,500', 'b-10,000',
                   'c-15,000', 'd-20,000')

#   Stuck here....i don't think this is the right track...
realans1 = MusicQuiz('The answer is' + self.realans)
realans2 = MusicQuiz
realans3 = MusicQuiz
realans4 = MusicQuiz
realans5 = MusicQuiz
realans6 = MusicQuiz
realans7 = MusicQuiz
realans8 = MusicQuiz
realans9 = MusicQuiz
realans10 = MusicQuiz

# Output
print(MusicQuiz.question(ques1))
print(MusicQuiz.question(ques2))
print(MusicQuiz.question(ques3))
print(MusicQuiz.question(ques4))
print(MusicQuiz.question(ques5))
print(MusicQuiz.question(ques6))
print(MusicQuiz.question(ques7))
print(MusicQuiz.question(ques8))
print(MusicQuiz.question(ques9))
print(MusicQuiz.question(ques10))
print('--THE REAL ANSWERS ARE BELOW-----')  # THIS DOESN"T TRACK PLAYER SCORES

"""
