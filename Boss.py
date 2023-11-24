from Task import Task
from Manager import QueueClient

class Boss(QueueClient):
    def __init__(self):
        super().__init__()
        for t in range(10):
            task = Task(t)
            self.tasks.put(task)
        print("fini")
            
if __name__ == "__main__":
    boss=Boss()
