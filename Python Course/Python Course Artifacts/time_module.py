import time

print(time.ctime(1000000))
print(time.time()) #return current seconds since epoch
time_object = time.localtime()
local_time = time.strftime('%B %d %Y %H:%M:%S',time_object) #see official python documentation for more info
print(local_time)

time_string = "20 April, 2020"
time_object = time.strptime(time_string,'%d %B, %Y')
print(time_object)
