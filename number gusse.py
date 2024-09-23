import random #library define


def game(): #funcation define
 
 user_input=int(input("enter your number:")) #user_input 
 computer=random.randint(1,100) #random number select by the compuer in range 100
 attemt=1  #number off attemt
 while user_input!=computer:# while loop for untail the answer is not get it 
    
    attemt=attemt+1
    if user_input>computer: #1st condition cheak
        print("select lower number")
        
    else:  # else condition
        print("select high number")
     
    user_input=int(input("try agian:"))  #second time   
 print(f"you answer is correct in number of {attemt}")
     
     #no. off attempt print
game()    

