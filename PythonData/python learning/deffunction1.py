#  Function and DOcstring
#a = 5
#b = 4
#c = sum((a, b)) #syntax of predefined function and builtin function sum()
#print(c)

"""def a1():                                   #creating your funciton or defination syantax : def name()
    print("making my first function")       #function defination or defination body
    print(a1())                             #print a function
    a1()                                    #call a function"""
"""
def function1(a, b):                            # addition function as function1
    print("addition of a+b",a+b)
function1(23, 34)
"""

def ae(a, b):
    """this is average function of two numbers"""  #this a doc string and there implimentation this is one kind of comment but is show when you type in first in  function  as it is fucntion
    average = (a+b)/2
    return average #return bqz need to store the value of avg in v 
#print(ae(3, 5))
#v = ae(4, 6)    #sotre value of ae function in v variable 
#print(v)    #print v
print(ae.__doc__) # this is a method of printing docstring in function when multiple function are in program this is help to you which function where and how use

