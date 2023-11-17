from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from django.contrib.auth.models import User
from section.models import Section
from task.models import Task

class TaskSerializer(serializers.ModelSerializer):
	user = serializers.PrimaryKeyRelatedField(queryset=User.objects.none())

	# remove objects not owned by the user in the options from browseable API as well
	def __init__(self, *args, **kwargs):
		super(TaskSerializer, self).__init__(*args, **kwargs)
		request = self.context.get('request')
		if request and request.user:
			user =  request.user
			self.fields['user'].queryset = User.objects.filter(id=user.id)
			self.fields['section'].queryset = Section.objects.filter(user=user.id)

	validators = [
			UniqueTogetherValidator(
					queryset=Task.objects.all(),
					fields=['user', 'section', 'priority']
			)
	]

	class Meta:
		model = Task
		fields = '__all__'