# This is a sample module to demonstrate the use of __name__ in Python.

def myFunc():
    print("hello World!")
    
# myFunc()
# print(__name__)

if __name__ == "__main__":
    # if this code is directly executed by running the file its present in.

    print("We are running this file code directly.")
    myFunc()
    print(__name__)