from rest_framework import serializers

from task.models import Task

class TaskSerializer(serializers.ModelSerializer):
	user = serializers.PrimaryKeyRelatedField(read_only=True)

	# on save, add the request.user as the user
	def create(self, validated_data):
		validated_data['user'] = self.context['request'].user
		return super().create(validated_data)

	class Meta:
		model = Task
		fields = '__all__'