"""
MULTITHREADING

1. Process
- A running program.
- Created by the operating system.
- Has its own memory.

2. Thread
- Smallest unit of execution inside a process.
- Multiple threads can exist in one process.
- Threads share the same memory.

3. Multithreading
- Running multiple threads in one process.
- Makes tasks faster by performing work concurrently.

4. Sequential Execution
- One task starts only after the previous task finishes.
- Slow for port scanning.

5. ThreadPoolExecutor
- Manages a pool of reusable threads.
- Uses max_workers to limit the number of concurrent threads.
- Efficient and widely used in Python.

"""

from concurrent.futures import ThreadPoolExecutor
"""
from : go to specific module and bring only the thing i need
concurrent : python inbuilt module
futures : a folder under concurrent : a task that has started, but whose result may come later
Thread pool executor : It is a class provided by Python.
                       Its job is:
                    Create worker threads.
                    Manage those threads.
                    Reuse them.
                    Assign tasks automatically.
                    Think of it as a manager.
Important:
Importing ThreadPoolExecutor DOES NOT create any threads.
It only makes the class available for use.
"""
# with ThreadPoolExecutor(max_workers= 10) as executor:
#     print("Thread pool created")
#     print("program finished")
"""
LESSON 2

with
- Python keyword.
- Automatically manages resources.
- Automatically closes the ThreadPoolExecutor after use.

ThreadPoolExecutor()
- Creates an executor object.
- Creates and manages worker threads.

max_workers
- Maximum number of worker threads.
- Common values for a beginner scanner: 50–200.

as
- Stores the created object in a variable.

executor
- Variable name for the ThreadPoolExecutor object.
- Used to submit tasks.

Important:
Creating a ThreadPoolExecutor creates the thread pool.
The threads remain idle until tasks are submitted with executor.submit().

ThreadPoolExecutor does NOT divide work equally.
Each worker takes one task.
When a worker finishes, it immediately takes the next available task.
Fast workers may complete more tasks than slow workers.
This dynamic scheduling makes ThreadPoolExecutor efficient.
"""
#  now we created multiple threads and they still haven't yet assigned work now we are gonna assign them work
def scan_port(port): # here we are defining a function called scan_port and port is variable
    print(f"scanning port {port}")  # this is input taking as vairable port

with ThreadPoolExecutor(max_workers= 10) as executor:  # this code is making workers (threads) as variable executor
    print("Thread pool created")  # this line will be only printed if successfully when the threads are created
    for port in range(1,1025):    # this is ports range from (1,1025)
        executor.submit(scan_port, port)  # this code is making to assign the work for threads
        print('scanned successfuly')   # after assigning of work and completing task this will be printed


