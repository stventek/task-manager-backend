from rest_framework import serializers

from section.models import Section
from django.contrib.auth.models import User

from rest_framework.validators import UniqueTogetherValidator

from task.serializers import TaskSerializer

class SectionSerializer(serializers.ModelSerializer):
	user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
	tasks = TaskSerializer(many=True, read_only=True)

	# remove objects not owned by the user in the options from browseable API as well
	def __init__(self, *args, **kwargs):
		super(SectionSerializer, self).__init__(*args, **kwargs)
		request = self.context.get('request')
		if request and request.user:
			user =  request.user
			self.fields['user'].queryset = User.objects.filter(id=user.id)

	validators = [
		UniqueTogetherValidator(
			queryset=Section.objects.all(),
			fields=['user', 'priority']
		)
	]

	class Meta:
		model = Section
		fields = '__all__'
		