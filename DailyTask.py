import json
import os

class TaskManager:
   def __init__(self):
       self.task=[]
       self.f_name="tasks.json"
       
   def load_task(self):
       if os.path.exists(self.f_name):
          try:
             with open(self.f_name, "r") as file:
                self.task=json.load(file)
                
          except Exception as e:
             self.task=[]
             
       else:
          self.task=[]
          
   def save_task(self):
      with open(self.f_name, "w") as file:
         json.dump(self.task, file)
         
   def add_task(self):
      tittle=input("Write the Title: ")
      description=input("Write the Description: ")
      task={
         "tittle": tittle,
         "description": description
      }
      self.task.append(task)
      self.save_task()
      print("Successfully Task Added")
      
      
   def view_task(self):
      if len(self.task)==0:
         print("There is no task assign")
         
      else:
         print("Your Task List")
         for i in range(len(self.task)):
            print (str(i+1) + ". Tittle: " + self.task[i]["tittle"])
            print ("Description: " + self.task[i]["description"])
         
   def delete_task(self):
      if(len(self.task)==0):
         print("There is no task availabe for delete")
         
      else:
         self.view_task()
         taskNo=input("Enter Task Number to Delete: ")
         
         if taskNo.isdigit():
            number=int(taskNo)
            if(number>=1 and number<=len(self.task)):
               del self.task[number-1]
               self.save_task()
               print("Successfully Task Deleted")
            else:
                print ("Task Number Is not available")
                
         else:
             print("Please inter Valid Task Number")
         
tm=TaskManager()
tm.load_task()

while True:
   print("\n===== Task Tracker =====")
   print("1. Add Task")
   print("2. View Tasks")
   print("3. Delete Task")
   print("4. Exit")
   
   c=input("Enter the Number You want to do: ")
   if c=="1":
      tm.add_task()
      
   elif c=="2":
      tm.view_task()
      
   elif c=="3":
      tm.delete_task()
      
   elif c=="4":
      print("Exit The program")
      break;
      
   else: 
      print("Enter a number from 1 to 4")
                     
     