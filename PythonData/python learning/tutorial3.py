#how to use variables and how type casting is done
var="7 " #string
var1=45 #int
var2=62.5 #float
var3="8" #string
var4="name: "
var5="prathmesh"

#print(type(var3)) 
#print(type(variable_name))  it  is used for check which type of variable
print(int(var)+var2)#type casting of variable 1 in integer
print(20 * str(int(var)+int(var3))) #adding one and two variables called concat  method
print(100 * var4 + var5)#adding of variables and disply them and multiple time disply using this syntax no*
# if you want to print integer in timeslap first change there type into string like print(timeslap * str(int (v) + int(v1))) like row no.11

print("enter your no")
inpnum = input() #inpnum is used for input number form user this is the syantax 
print("Your no is=", int(inpnum)+10) #it is use to print user get value


#excersies :- making calculator adding two no.
"""
print("enter your first no.")
n1 = input()
print("eneter your second no.")
n2 = input()
print("your addition is", int(n1)+int(n2))

"""