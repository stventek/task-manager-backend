from rest_framework import serializers

from section.models import Section
from django.contrib.auth.models import User

class SectionSerializer(serializers.ModelSerializer):
  user = serializers.PrimaryKeyRelatedField(read_only=True)

  # on save, add the request.user as the user
  def create(self, validated_data):
    validated_data['user'] = self.context['request'].user
    return super().create(validated_data)

  class Meta:
    model = Section
    fields = '__all__'