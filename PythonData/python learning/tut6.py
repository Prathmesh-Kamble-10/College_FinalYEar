                # Dictionary and its Function

d1 = { "jhon":"chapati", "samiksha":"creame roll", "laster":"hacking","farmer":{"god":"lifesaver","farm":"grass"}}# u can add dictionary in dictionary
#print(type(d1)) #checking type of varaible
#print(d1["jhon"])
#print(d1["farmer"]["farm"]) # how to access dictonary in dictionary
#d1["sameer"] = "labour" #add dictionary
#del d1["sameer"] #remove or delete dictionary 
#print(d1)
#d2 = d1.copy() #making the copy of d1 bqz del any dictionary its deleted from another dictionary when they are equal or coyped
#del d2["jhon"]
#d1.update({"leena":"toffy"}) #update function use for update dictionary
#print(d2, d1)  #print both dictionary one time
#print(d2.keys()) #print only keys not itams
#print(d2.items())  #print items and keys

                        #excercise :create a dictionary and take_input from user and return meaning of word from the dictionary
dic = {"Apple":" It is the fruit","Fun":"gamat","Appriciate":"Sahamat","Tall":"laamb","Absent":"gera haajar","Mobile":"phone"}
user = input("Search : ") #here is get input in user varaible
b=user.capitalize() # and b store inputs of user variable in capitalize form using capitalize function (note : its change the there case in runtime. but bydefualt its normal case )and input proceed in first letter capitalzie form 
print(user," : ", dic[b]) #bqz store the value of var_user in var_b so print dic[b] as b and user is print for typed function print as first word

"""
                    #excercise : create a user record and get input from user and display it

name = {"ravi_data":{"roll_no":47,"age":21,"filed":"arts","no":7874126550,"email":"ravi@abc.com"},
"vishal_data":{"roll_no":91,"age":20,"dep":"computer","no":1234567890,"email":"vishal@abc.com"},
"abhishek_data":{"roll_no":22,"age":20,"dep":"computer","no":9112303232,"email":"abhi3232@abc.com"},
"azim_data":{"roll_no":11,"age":22,"dep":"civil","no":7894561230,"email":"azim@abc.com"},
"rohit":{"roll_no":87,"age":20,"dep":"mechanical","no":9632214587,"email":"rohit@abc.com"}}
print("User data :")
user = input()
print("result :", name[user]) 
"""






