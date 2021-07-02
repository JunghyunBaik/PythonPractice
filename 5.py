'''
Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use __init__ method to construct some parameters
'''
class Methods:
    def __init__(self):
        self.result = ''

    def getString(self):
        self.result = input('your str : ')

    def printString(self):
        print(self.result.upper())

method1 = Methods()
method1.getString()
method1.printString()