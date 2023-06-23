#multiprocessing = run in parallel on different cpu core
    #better for heavy cpu usage 
from multiprocessing import Process, cpu_count
import time

def counter (num):
    count = 0
    while count < num:
        count +=1

def main():
    a = Process(target = counter,  args = (500000000,))
    b = Process(target = counter, args = (500000000,))
    b.start()
    a.start()
    a.join()
    b.join()
    print("Finished in ",time.perf_counter(),"seconds.")        
    
if __name__ == 'main':
    main()

