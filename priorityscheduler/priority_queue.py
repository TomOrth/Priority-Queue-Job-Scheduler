class PriorityQueue(object):
    """A Min-Heap based Priority Queue"""
    
    def __init__(self):
        """ Initializes a list of custom Jobs to run"""
        self.jobs = []

    def _parent(self, i): 
        """ Function to get a parent node of a node in the PriorityQueue (Min-Heap)
        Args:
            i - index of the current item in the list of jobs
        Returns:
            The parent item to the current item in the list of jobs
        """
        return int((i-1)/2)

    def _left(self, i):
        """ Function to get the left child of a node in the Priority Queue (Min-Heap)
        Args:
            i - index of the current item in the list of jobs
        Returns:
            The left child of the current item in the list of jobs
        """
        return 2*i+1

    def _right(self, i):
        """ Function to get the right child of a node in the Priority Queue (Min-Heap)
        Args:
            i - index of the current item in the list of jobs
        Returns:
            The right child of the current item in the list of jobs
        """
        return 2*i+2
    
    def _rotateUp(self, loc):
        """ Sorts the Priority Queue (Min-Heap) based on the jobs' priority when a new job is added
        Args:
            loc - index of the item added to the Priority Queue (Min-Heap)
        """
        while(self._parent(loc) >= 0 and self.jobs[loc].priority < self.jobs[self._parent(loc)].priority):
            self._swap(self._parent(loc), loc)
            loc = self._parent(loc)

    def _rotateDown(self, index):
        """ Sorts the Priority Queue (Min-Heap) based on the jobs' priority when a job is popped
        Args:
            index - index of the item to rotate down in the Priority Queue (Min-Heap)
        """

        smallest = index
        l = self._left(index)
        r = self._right(index)
        if (l < len(self.jobs) and self.jobs[l].priority < self.jobs[index].priority):
            smallest = l
        if (r < len(self.jobs) and self.jobs[r].priority < self.jobs[smallest].priority):
            smallest = r
        if (smallest != index):
            self._swap(index, smallest)
            self._rotateDown(smallest)
    
    def _swap(self, orig, new):
        """ Standard swap function
        Args:
            orig - the original index of the item to be swapped
            new - the new index of the item being swapped
        """

        temp = self.jobs[orig]
        self.jobs[orig] = self.jobs[new]
        self.jobs[new] = temp

    def push(self, job):
        """ Adds a job the Priority Queue (Min-Heap) and then sorts the jobs
        Args:
            job - a new Job object to be added to the Priority Queue (Min-Heap)
        """
        self.jobs.append(job)
        self._rotateUp(len(self.jobs)-1)
    
    def pop(self):
        """ Removes the job with the lowest priority from the Priority Queue (Min-Heap) and then resorts the jobs
        Returns:
            The newly removed job
        """
        job = self.jobs[0]
        self.jobs[0] = self.jobs[len(self.jobs)-1]
        self.jobs.pop()
        self._rotateDown(0)
        return job

    def empty(self):
        """  Checks to see if the Priority Queue (Min-Heap) is empty
        Returns:
            A boolean, representing whether or not the Priority Queue (Min-Heap) is empty
        """
        return len(self.jobs) == 0