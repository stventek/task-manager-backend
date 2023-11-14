from django.urls import include, path
from rest_framework import routers

from task.views import TaskViewSet

router = routers.DefaultRouter()

router.register(r'task', TaskViewSet)

urlpatterns = [
  path('', include(router.urls), ),
]