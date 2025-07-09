from django.urls import include, path
from rest_framework import routers
from .views import TestView

router = routers.DefaultRouter()

urlpatterns = [
    path('test/', TestView.as_view(), name='test-view'),
]+router.urls