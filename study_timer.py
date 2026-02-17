import time
import random #to make random task choices

topic=input("Enter topic: ").strip()
#incase the the subject is not mentioned the code will not run.strip() to clean outer spaces
while topic=="":
    print("Subject cannot be empty. Please enter a subject.")
    topic = input("Enter topic: ").strip()
#list for task to be given during breaks
break_tasks = ["Stretch", "Drink water", "Eye exercise","Talk to parents","Dance to a pop song"]
#session starts
print("Starting study session for",topic)
#time duration of the study period
for count_down in range(10,0,-1):
    print(count_down)
    time.sleep(1)
#stop the session and break time.
print("Break time🎉🎉! Try:",random.choice(break_tasks))
