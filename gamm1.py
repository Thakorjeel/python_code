

#game program
import random   #use random 
def game(com,us):  #fun define
        if (com==us ): #condition
          return 0
        if (com==0 and us==1):
          return 2


        
        if (com==1 and us==2):
           return 2
        if (com==2 and us==0):
           return 2

        
        return 1 
us=int(input("0 for stonne,2 for paper,1 for scissor:"))
com= random.randint(0,2)
print("you choose:" ,us)
print("computer choose:",com)

socre= game(com,us)
if (socre==0):
       print("draw")
elif(socre==1):
       print("you win ")
else:
       print("you losse")
while socre!=1:
     us=int(input("0 for stonne,1 for scissor,2 for paper:"))
     com= random.randint(0,2)
     game(com,us)
     print("you choose:" ,us)
     print("computer choose:",com)
     socre= game(com,us)
     if (socre==0):
          print("draw")


     elif(socre==2):
       print("you losse")
     elif(socre==1):    
       print("you win")