from apscheduler.schedulers.background import BackgroundScheduler
from api import data_collector
from app import settings


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(data_collector.collect_data, 'interval', seconds=settings.UPDATE_IN_SECONDS)
    scheduler.start()
