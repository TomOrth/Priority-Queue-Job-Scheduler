# Priority-Queue-Job-Scheduler
Custom Priority Queue (Min-Heap) to run jobs in priority order

# Installing

`pip install priorityscheduler`

# How It Works

The queue takes in an object that inherit from the type `Job`.  Once the jobs are added to the queue, it runs the Min-Heap algorithm to sort the jobs by their `priority` property.  When the jobs are popped by the `pop` function, it again performs the Min-Heap algorithm to re-sort the jobs.  Please see the [Example](#example) section and [example.py](example.py) for an example this library

# Example

```python
from priorityscheduler import PriorityQueue, Job

class PrintJob(Job):

    def __init__(self, priority):
        super().__init__(priority)
    
    def run_job(self):
        print("ran job with priority {}".format(self.priority))

j1 = PrintJob(1)
j2 = PrintJob(2)
j3 = PrintJob(3)
j4 = PrintJob(4)

pq = PriorityQueue()
pq.push(j2)
pq.push(j3)
pq.push(j1)
pq.push(j4)

while not pq.empty():
    pq.pop().run_job()
```

# Authors/Contributors

* Tom Orth [TomOrth](https://www.github.com/TomOrth)
