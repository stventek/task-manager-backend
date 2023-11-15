from django.http import QueryDict
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

	def create(self, request, *args, **kwargs):
		if isinstance(request.data, QueryDict): # check if is instance of QueryDict so it's easier to unit test
				request.data._mutable = True
		request.data['user'] = request.user.id
		return super().create(request, *args, **kwargs)