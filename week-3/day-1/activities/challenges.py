#Challenge 1, use loops to print hello world 13 times.
#for i in range(1, 14):
    #print(i,"Hello World")
   
#counter = 0
 
#while counter < 14:
    #print(counter,"Hello World")
    #counter += 1


#Challenge 2 

#from random import randint

#for x in range (0,6):
    #random_number = randint(1,30)
    #if (random_number%7 == 0):
        #print(f"Yes, the number {random_number} is diviible by 7.")
    #else:
        #print(f"The number {random_number} is not divisible by 7.")


#Challenge 3
#Times table generator

times_table = int(input("Please enter the times tables you want to see or 13 and above to exit> "))
while times_table < 20:    
    for index in range(1,20):
        result = index * times_table
        print(f"{times_table} x {index} = {result}")
    times_table = int(input("Please enter the times tables you want to see or 13 and above to exit> "))
