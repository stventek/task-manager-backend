from common.filter import AnyModelFilter
from task.models import Task

class TaskFilter(AnyModelFilter):
  class Meta:
    model = Task
    fields = '__all__'
      