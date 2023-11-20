from django.http import QueryDict
from section.filter import SectionFilter
from section.models import Section
from section.serializers import SectionSerializer

from rest_framework import viewsets

class SectionViewSet(viewsets.ModelViewSet):
	queryset = Section.objects.all()
	serializer_class = SectionSerializer
	filterset_class  = SectionFilter

	def get_queryset(self):
		return Section.objects.filter(user=self.request.user)

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
		return super().partial_update(request, *args, **kwargs)
