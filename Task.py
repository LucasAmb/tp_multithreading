import time

import json
import numpy as np


class Task:
    def __init__(self, identifier):
        self.identifier = identifier
        # choosee the size of the problem
        self.size = np.random.randint(300, 3_000)
        # Generate the input of the problem
        self.a = np.random.rand(self.size, self.size)
        self.b = np.random.rand(self.size)
        # prepare room for the results
        self.x = np.zeros((self.size))
        self.time = 0

    def work(self):
        start = time.perf_counter()
        self.x = np.linalg.solve(self.a, self.b)
        self.time = time.perf_counter() - start

    def to_json(self) -> str :
        data = json.dumps({"id":self.identifier, "size":self.size,
                            "a":self.a.tolist(), "b":self.b.tolist(), "x":self.x.tolist(), "time": self.time})
        return data

    @classmethod
    def from_json(cls, text: str) -> "Task":
        jsonRecup=json.loads(text)
        obj = cls(jsonRecup["id"])
        obj.a = np.array(jsonRecup["a"])
        obj.b = np.array(jsonRecup["b"])
        obj.x = np.array(jsonRecup["x"])
        obj.size = np.array(jsonRecup["size"])
        obj.time = jsonRecup["time"]
        return obj

    def __eq__(self, other: "Task") -> bool:
        if isinstance(other, Task):
            if np.array_equal(self.a, other.a) and np.array_equal(self.b, other.b) and np.array_equal(self.x, other.x):
                return True
        return False
    
if __name__ == "__main__":
    taskCree = Task("0")
    txt = taskCree.to_json()
    taskReceive = Task.from_json(txt)
    print(taskCree == taskReceive)