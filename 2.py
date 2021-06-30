'''
Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''

num = int(input('put your number : '))

def factorial(i):
    j = 1
    for k in range(i):
        j *= k+1
    return j
print(factorial(num))
