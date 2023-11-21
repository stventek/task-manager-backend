from django.db import models
from common.models import BaseModel
from section.models import Section

class Task(BaseModel):
	user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	priority = models.TextField()
	section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='tasks')
	description = models.TextField(default=None, blank=True, null=True)
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name

	class Meta:
		unique_together = ('user', 'priority', 'section')
