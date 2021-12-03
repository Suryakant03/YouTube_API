from datetime import datetime

from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Video

from api.serializers import VideoSerializer


VIDEOS_URL = reverse('api:video-list')


class PublicVideoslistApiTests(TestCase):
    """Test the publicaly available Videos API"""

    def setUp(self):
        self.client = APIClient()

    def test_videoslist_api(self):
        """Test retrieving videos"""
        Video.objects.create(
            vid="1",
            title="Test Title A",
            description="Test Description A",
            publishing_datetime=datetime.now(),
            thumbnail_URLs="http://testurl1",
        )
        Video.objects.create(
            vid="2",
            title="Test Title B",
            description="Test Description B",
            publishing_datetime=datetime.now(),
            thumbnail_URLs="http://testurl2",
        )

        res = self.client.get(VIDEOS_URL)

        videos = Video.objects.all()
        serializer = VideoSerializer(videos, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
