from turtle import *
from functions import *
from datetime import datetime
from time import *
now = datetime.now()
speed(1000)
goto(0,-30)
circle(50)
goto(0,0)
left(90)
forward(30)
while True:
 break
 clear()
 current_time = datetime.now().strftime("%H:%M:%S")
 write(current_time,font=("Arial", 20, "bold"))
 sleep(1)
mainloop()