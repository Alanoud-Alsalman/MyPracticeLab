import random
import time


time_slice = random.randint(1,10)

start_time = time.clock()

process_list = []

for i in range(10):
  temp = input('Enter p%d'%(i))
  process_list.append(temp)
  
end_time = time.clock()


print 'timer = %d'%(end_time - start_time)
