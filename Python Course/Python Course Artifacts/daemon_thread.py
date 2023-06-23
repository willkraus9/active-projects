#demon thread - run in background program (long-running process)
import threading
import time

def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count+= 1
        print('logged in for: ',count," seconds")
        
x = threading.Thread(target = timer, daemon=True)#can't normally close program; must make timer = demon thread
x.start()
answer = input("do you wish to exit?")