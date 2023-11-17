from django.http import QueryDict
from task.filter import TaskFilter
from task.models import Task
from task.serializers import TaskSerializer
from rest_framework import viewsets, exceptions

class TaskViewSet(viewsets.ModelViewSet):
	queryset = Task.objects.all()
	serializer_class = TaskSerializer
	filterset_class  = TaskFilter

	def get_queryset(self):
		# request.user scoped queryset to ensure object ownership 
		return Task.objects.filter(user=self.request.user, section__user=self.request.user)

	def set_user_in_request_data(self, request):
		if isinstance(request.data, QueryDict):
				request.data._mutable = True
		request.data['user'] = request.user.id

	def create(self, request, *args, **kwargs):
		self.set_user_in_request_data(request)
		return super().create(request, *args, **kwargs)

	def update(self, request, *args, **kwargs):
		self.set_user_in_request_data(request)
		return super().update(request, *args, **kwargs)

	def partial_update(self, request, *args, **kwargs):
		self.set_user_in_request_data(request)
		return super().update(request, *args, **kwargs)

	def ensure_ownership(self, serializer):
		user = serializer.validated_data['user']
		section = serializer.validated_data['section']
		if section.user != self.request.user or user != self.request.user:
			raise exceptions.PermissionDenied("You have no ownership for this operation")
		serializer.save()

	def perform_create(self, serializer):
		self.ensure_ownership(serializer)

	def perform_update(self, serializer):
		self.ensure_ownership(serializer) 