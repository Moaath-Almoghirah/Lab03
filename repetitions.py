x= int(input("Enter a number of repetitions\n"))

#the decorator
def hello_repetition(func):
    for i in range(x):
        func()

def hello():
    print ('Hello')

#calling the decorator
hello_repetition(hello)

