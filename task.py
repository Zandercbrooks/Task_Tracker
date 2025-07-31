class Task:
    def __init__(self,description):
        self.description = description
        self.progress = "todo"

    def update(self, update):
        self.description = update

    def markInProgress(self):
        self.progress = "in-progress"

    def markDone(self):
        self.progress = "done"

    def getDescription(self):
        return self.description
    def getProgress(self):
        return self.progress
    