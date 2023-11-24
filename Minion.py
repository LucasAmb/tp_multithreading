from Manager import QueueClient

class Minion(QueueClient):
    def __init__(self):
        super().__init__()
    
    def run(self):
        taskToBeDone=self.tasks.get()
        print("passe2")
        if(taskToBeDone is not None):
            print("Debut travail sur :", taskToBeDone.identifier)
            taskToBeDone.work()
            self.results.put = taskToBeDone.x
            print(" résultat pour la tâche ", taskToBeDone.identifier, ": \n")
            print(taskToBeDone.x, "\n")

if __name__ == "__main__":
    minion = Minion()
    while(1):
        print(minion.tasks)
        minion.run()
        print("passe1")


