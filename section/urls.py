from django.urls import include, path
from rest_framework import routers
from section.views import SectionViewSet

router = routers.DefaultRouter()

router.register(r'section', SectionViewSet)

urlpatterns = [
  path('', include(router.urls), ),
]