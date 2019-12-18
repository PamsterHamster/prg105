
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

