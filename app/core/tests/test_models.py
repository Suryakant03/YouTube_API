from django.test import TestCase
from core.models import Video
from datetime import datetime


class ModelTests(TestCase):

    def test_create_video_with_data_successful(self):
        """Creating a new video with correct data is successfull"""
        video_id = '1'
        video_title = 'Test Title'
        video_description = 'Test Description'
        video_publishing_datetime = datetime.now()
        video_thumbnail_URLs = 'http://test.com'

        video = Video.objects.create(
            vid=video_id,
            title=video_title,
            description=video_description,
            publishing_datetime=video_publishing_datetime,
            thumbnail_URLs=video_thumbnail_URLs,
        )

        self.assertEqual(video.vid, video_id)
        self.assertEqual(video.title, video_title)
        self.assertEqual(video.description, video_description)
        self.assertEqual(video.publishing_datetime, video_publishing_datetime)
        self.assertEqual(video.thumbnail_URLs, video_thumbnail_URLs)
