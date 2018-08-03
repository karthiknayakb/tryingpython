import multiprocessing as mp
import random
# Define an output queue
output = mp.Queue()

# define a example function
def rand_string(numa, output):
    """ Generates a random string of numbers, lower- and uppercase chars. """
    rand_str = sum(numa)
    #print rand_str
    output.put(rand_str)

def getrandomarr(n,output):
    a=[]
    for i in range(n):
        a.append(random.randint(1,101))
    output.put(a)
    #return a

# Setup a list of processes that we want to run
processes = [mp.Process(target=getrandomarr, args=(25, output)) for x in range(900)]

# Run processes
for p in processes:
    p.start()

# Exit the completed processes
for p in processes:
    p.join()

# Get process results from the output queue
results1 = [output.get() for p in processes]

processes2 = [mp.Process(target=rand_string, args=(x, output)) for x in results1]

for p in processes2:
    p.start()
for p in processes2:
    p.join()

print len(results1)