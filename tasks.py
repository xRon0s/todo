class TaskManager:
  def __init__(self):
    self.tasks = []

  def add_task(self, task):
    self.tasks.append(task)

  def delete_task(self, index):
    if 0 <= index < len(self.tasks):
      del self.tasks[index]

  def get_tasks(self):
    return self.tasks