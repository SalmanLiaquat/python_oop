# Encapsulation -> binding data and method together into a class while restricting the access to some extend
'''
-> public
->private
->protected: not accessible outside the class (work in cpp and othe but don't in python)
'''
# Use Getters & Setters for controlled access.

class Bank:
    __acc_holder = None
    __acc_no = None
    __balance = None

    def __init__(self, acc_holder, acc_no, balance):
        self.__acc_holder = acc_holder
        self.__acc_no = acc_no
        self.__balance = balance

    def get_acc_holder(self):
        return self.__acc_holder

    def get_balance(self):
        return self.__balance

    def get_acc_no(self):
        return self.__acc_no

acc_holder = input("Enter account holder name: ")
acc_no = input("Enter account number: ")
balance = float(input("Enter account balance: "))
obj =Bank(acc_holder,acc_no,balance)
print(obj.get_acc_holder())
print(obj.get_acc_no())
print(int(obj.get_balance()))
