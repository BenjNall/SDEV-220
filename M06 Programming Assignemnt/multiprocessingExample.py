import multiprocessing
import time
import random
from datetime import datetime

# Function to be executed by each process
def print_time():
    # Generate a random number between 0 and 1
    sleep_time = random.uniform(0, 1)
    
    # Make the process sleep for the random amount of time
    time.sleep(sleep_time)
    
    # Print the current time after the sleep
    print(f"Process {multiprocessing.current_process().name} - Time: {datetime.now()}")

if __name__ == '__main__':

    # Create a list to hold processes
    processes = []
    
    # Create 3 separate processes
    for i in range(3):
        process = multiprocessing.Process(target=print_time, name=f"Process-{i+1}")
        processes.append(process)
    
    # Start all the processes
    for process in processes:
        process.start()
    
    # Wait for all processes to complete
    for process in processes:
        process.join()