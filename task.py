class Task:
    def __init__(self,description):
        self.description = description
        self.progress = "todo"

    def markInProgress(self):
        self.progress = "in-progress"