# exercise 2 : Design a calculater which will correcly solve all the problems exvept the follwoing one :
# 45 * 3 =555, 56+9 = 77,56/6 = 4
a =int(input("Enter your first no."))
b =int(input("Enter your second no."))
ch = input("Which operation you perfoem"+'+,-,/,*\t') # simple print outs of and getting choice of addition and substration or division and multiplication
if a==56 and b==9 or a==9 and b==56 or ch=='+':
        print("77")
elif a==56 and b==6 or a==6 and b==56 or ch=='/':
        print("4")
elif a==45 and b==3 or a==3 and b==45 or ch=='*':
        print("555")
elif ch=='+':
        c = a+b
        print("Your addition is : ",c)
elif ch=='-':
        c = a-b
        print("Your substraction is : ",c)
elif ch=='*':
        c = a*b
        print("Your Multiplication is : ",c) 
elif ch=='/':
        c = a/b
        print("Your division is : ",c)
else:
        print("Error")