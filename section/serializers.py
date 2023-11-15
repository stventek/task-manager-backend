from rest_framework import serializers

from section.models import Section
from django.contrib.auth.models import User

from rest_framework.validators import UniqueTogetherValidator

class SectionSerializer(serializers.ModelSerializer):
	user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

	validators = [
		UniqueTogetherValidator(
			queryset=Section.objects.all(),
			fields=['user', 'priority']
		)
	]

	class Meta:
		model = Section
		fields = '__all__'
		