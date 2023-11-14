from common.filter import AnyModelFilter
from section.models import Section

class SectionFilter(AnyModelFilter):
  class Meta:
    model = Section
    fields = '__all__'
