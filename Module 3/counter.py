import time 
def timer(seconds): 
    while seconds > 0: 
        mins = int(seconds/60) 
        sec = int(seconds%60) 
        timer = f"{mins}:{sec}" 
        print(timer) 
        seconds-=2 
        time.sleep(0.5)
    print("timeup")
seconds = int(input("enter the time in number of seconds : " ))
timer(seconds)
