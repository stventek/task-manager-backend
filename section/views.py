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
  