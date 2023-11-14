from rest_framework import serializers

from section.models import Section

class SectionSerializer(serializers.ModelSerializer):
  user = serializers.StringRelatedField()

  class Meta:
    model = Section
    fields = '__all__'