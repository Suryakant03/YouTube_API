from django.urls import path

from api import views


app_name = 'api'

urlpatterns = [
    path('videos/', views.VideoViewSet.as_view(), name="video-list")
]

