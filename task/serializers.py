from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from django.contrib.auth.models import User
from task.models import Task

class TaskSerializer(serializers.ModelSerializer):
	user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

	validators = [
			UniqueTogetherValidator(
					queryset=Task.objects.all(),
					fields=['user', 'section', 'priority']
			)
	]

	class Meta:
		model = Task
		fields = '__all__'