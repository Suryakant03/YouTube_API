from datetime import datetime, timedelta

import apiclient
from apiclient.discovery import build

from core.models import Video
from app import settings


def collect_data():
    print("Collecting Data...")
    api_keys = settings.GCP_API_KEYS
    curr_time = datetime.now()
    prv_time = curr_time - timedelta(seconds=1500)

    is_scraped = False
    res = {}
    for i in range(len(api_keys)):
        try:
            youtube = build("youtube", "v3", developerKey=api_keys[i])
            req = youtube.search().list(
                q=settings.SEARCH_QUERY,
                part="snippet",
                order="date",
                maxResults=50,
                publishedAfter=(prv_time.replace(microsecond=0).isoformat() + 'Z')
            )
            res = req.execute()
            is_scraped = True
        except apiclient.errors.HttpError as err:
            code = err.resp.status

            if not(code == 400 or code == 403):
                break
            else:
                if i + 1 < len(api_keys):
                    print("API Key Exhausted. Switching to APIKEY:", api_keys[i + 1])

        if is_scraped:
            break

    item_count = 0

    if is_scraped:
        for item in res['items']:
            try:
                vid = item['id']['videoId']
            except Exception as e:
                # print("ERROR while reading an item:", e)
                vid = None

            try:
                title = item['snippet']['title']
            except Exception as e:
                # print("ERROR while reading an item:", e)
                title = None

            try:
                description = item['snippet']['description']
            except Exception as e:
                # print("ERROR while reading an item:", e)
                description = None

            try:
                publishing_datetime = item['snippet']['publishedAt']
            except Exception as e:
                # print("ERROR while reading an item:", e)
                publishing_datetime = None

            try:
                thumbnail_URLs = item['snippet']['thumbnails']['default']['url']
            except Exception as e:
                # print("ERROR while reading an item:", e)
                thumbnail_URLs = None

            try:
                if Video.objects.filter(vid=vid).exists():
                    pass
                else:
                    Video.objects.create(
                        vid=vid,
                        title=title,
                        description=description,
                        publishing_datetime=publishing_datetime,
                        thumbnail_URLs=thumbnail_URLs
                    )
                item_count += 1
            except Exception as e:
                print("ERROR while reading an item:", e)

    if 'items' in res:
        print("Collected ", len(res['items']), "items, out of which ", item_count, "pushed to database!!!")
    else:
        print("No Data Collected. All APIKEYS are Exhausted!!!")
