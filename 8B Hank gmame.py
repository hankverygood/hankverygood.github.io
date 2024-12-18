import random,time,os

print("Welcome to the waiting game!")
print("\n\n")
print("Instruction\n")
print("You will be told to wait a number of second")
print("wait that number of seconds and then  press ENTER")
start=input("Are you ready?Press ENTER to start!!!!!!")
while start!="N":
    os.system('clear')
    waitingTime = random.randint(5,10)
    start = time.time()
    input("please wait for "+str(waitingTime)+"seconds")
    end = time.time()
    elapsed = end-start
    difference = abs(round(waitingTime-elapsed,2))

    print("You were"+str(difference)+"second out")
    if difference<0.5:
        print("Well done,You are good")
        print("Author:Hank")
    elif difference < 1:
         print("You did fine")
    else:
        print("You can do it better")
    start=input("Press ENTER to try again Or Press N to stop")
