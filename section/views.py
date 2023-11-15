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

	def create(self, request, *args, **kwargs):
		if isinstance(request.data, QueryDict): # check if is instance of QueryDict so it's easier to unit test
				request.data._mutable = True
		request.data['user'] = request.user.id
		return super().create(request, *args, **kwargs)