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
