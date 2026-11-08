from tasks import show_tasks , save_tasks , load_tasks
from dotenv import load_dotenv
import os

load_dotenv()

name = input("Enter your name: ")
print("welcome", name)

admin_mode = input("do you want to enter Admin Mode? (yes/no): ")
if admin_mode == "yes":
    password = input("Enter admin password: ")
    if password == os.getenv("admin_pass"):
        print("admin mode activated")
    else:
        print("enter wrong password")    

tasks = load_tasks()
count = int(input("How many tasks do you want to add ? : "))
for i in range(count):
    task_name = input("enter a task: ")
    priority = input("enter priority(low/medium/high): ").lower()
    task = {
        "name": task_name,
        "priority": priority,
    }
    tasks.append(task)

show_tasks(tasks)
save_tasks(tasks)