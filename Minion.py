from Manager import QueueClient

class Minion(QueueClient):
    def __init__(self):
        super().__init__()
    
    def run(self):
        #Get a task in the queue
        taskToBeDone=self.tasks.get()
        #Does the work of the task
        print("Debut travail sur :", taskToBeDone.identifier)
        taskToBeDone.work()
        #Add the result of the task to the result queue
        self.results.put = taskToBeDone.x
        print(" résultat pour la tâche ", taskToBeDone.identifier, ": \n")
        print(taskToBeDone.x, "\n")

if __name__ == "__main__":
    minion = Minion()
    while(1):
        print(minion.tasks)
        minion.run()


