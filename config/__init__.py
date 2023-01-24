# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.

from .celery_app import app as celery_app

__all__ = ("celery_app",)

celery_app.autodiscover_tasks()


@celery_app.task(bind=True)
def debug_task(self):
    print("Request: {0!r}".format(self.request))


celery_app.conf.beat_schedule = {}
