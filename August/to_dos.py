#python to do list my own 

#to do list: requirements- greetings, 
# have a button to add quick to-dos for today -> add to the list, 
# print list
 
# #
print (" Negi-- Nice to see you here ;) \n ") 
mylist = []
while mylist == []:
    print ("you ready to add? \n")
    tasks = input("Task:-> ")
    tasks = mylist.append(tasks)
    
    finish = input("fight more?(yes) or nah (no) \n")
    if finish == "yes":
        tasks = input("add:-> ")        
        tasks = mylist.append(tasks)
    else:
        print( f"Boom!\n {tasks}")
        break
       
     
 


 

    
