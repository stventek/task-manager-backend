from task.filter import TaskFilter

from task.models import Task
from task.serializers import TaskSerializer
from rest_framework import viewsets

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filterset_class  = TaskFilter

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)