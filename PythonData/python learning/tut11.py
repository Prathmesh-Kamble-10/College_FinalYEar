                    # break and continue statement
"""
i = 0
while(True): # while true and while 1 is a infinity code running phase 
    if(i+1<=5):
     i = i+1
     continue #continue statemnet runs before code of continue word when i values bigger than 5 its automatically run after code in whole while loop
    print(i+1, end=" ")
    if(i==40):   
        i = i+1
        break #stop the loop
    i = i + 1 # check tab and spaces also necessary extra spaces get wrong output 
    """

    #quiz : get input which is greater than 100 the input is not 100 or greater than 100 then again and again run loop

i = 0
while (True):
    i = int(input("Enter no. \n"))
    if (i>=100):
        print("ongratulation you are entered the no. is greater than 100 or equal to 100")
        break
    else:
        print("trying....\n")
        continue