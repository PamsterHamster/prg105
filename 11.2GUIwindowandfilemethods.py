# FILE 1: Employee Class


class Employee:
    def __init__(self, employee_name, employee_number):
        self.__employee_name = employee_name
        self.__employee_number = employee_number

    def set_employee_name(self, employee_name):
        self.__employee_name = employee_name

    def set_employee_number(self, employee_number):
        self.__employee_number = employee_number

    def get_employee_name(self):
        return self.__employee_name

    def get_employee_number(self):
        return self.employee_number

    def __str__(self):
        return "\nEmployee Name:  " + self.__employee_name + "\nEmployee number:    " + self.__employee_number


# test = Employee("Samantha Farlow", "000001")
#   print(test)


class ProductionWorker(Employee):
    def __init__(self, employee_name, employee_number, shift, pay_rate):
        Employee.__init__(self, employee_name, employee_number)

        self.__shift = shift
        self.__pay_rate = pay_rate

    def set_shift(self, shift):
        self.__shift = shift

    def set_pay_rate(self, pay_rate):
        self.__pay_rate = pay_rate

    def get_shift(self):
        return self.__shift

    def get_pay_rate(self):
        return self.__pay_rate

    def __str__(self):
        return "\nEmployee Name:  " + self.get_employee_name() + "\nEmployee Number:  " + self.get_employee_number() + \
               "\nShift:  " + self.__shift + "\nPay Rate:  " + self.__pay_rate


def __str___(self):
    return "\nEmployee name:  " + self.get_employee_name() + "\nEmployee Number:   " + self.get_employee_number() + \
           "\nShift:  " + self.__shift + "\nPay Rate:  " + self.__pay_rate


# test = ProductionWorker("Teri Gilbers", "00002",  "1", "30.00")
# print(test)

# ###########################################END FILE 1/BEGIN FILE 2####################################
# FILE 2:
"""

import employee

def main():
    name = input("Employee's Name:   ")
    number = input("Employee's Number:  ")
    shift = input("Employee's shift:  ")
    pay = input("Employee's pay rate:  ")

    new_employee = employee.ProductionWorker(name, number, shift, pay)
    print("nEmployee name:  " + new_employee.get_employee_name() + "\nEmployee Number:  " +
          new_employee.get_employee_number() + "\nShift: " + new_employee.get_shift() + "\nPay Rate: " +
          new_employee.get_pay_rate())

main()
"""
