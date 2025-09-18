class TaskManager:
    def __init__(self, tasks: List[List[int]]):
        self.q = []
        self.current_priority = {}
        self.completed = set()
        self.owners = {}
        for userId, taskId, priority in tasks:
          self.add(userId, taskId, priority)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        task = (-1 * priority, -1 * taskId)
        heapq.heappush(self.q, task)
        self.owners[taskId] = userId
        self.current_priority[taskId] = priority
        if taskId in self.completed:
          self.completed.remove(taskId)

    def edit(self, taskId: int, newPriority: int) -> None:
        self.add(self.owners[taskId], taskId, newPriority)

    def rmv(self, taskId: int) -> None:
        self.completed.add(taskId)

    def execTop(self) -> int:
        while self.q:
          priority, taskId = self.q[0]
          priority *= -1
          taskId *= -1
          if taskId in self.completed or priority != self.current_priority[taskId]:
            heapq.heappop(self.q)
          else:
            break

        if not self.q:
          return -1

        _, taskId = heapq.heappop(self.q)
        taskId *= -1
        self.completed.add(taskId)
        return self.owners[taskId]

# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()