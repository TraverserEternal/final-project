from django.db import models
from django_extensions.db.models import TimeStampedModel


class Data(TimeStampedModel):
    session = models.ForeignKey(
        verbose_name='session',
        to='trackers.Session',
        on_delete=models.CASCADE,
    )
    time = models.DateTimeField(
        verbose_name='time',
    )
    x = models.FloatField(
        verbose_name='x (m)',
    )
    y = models.FloatField(
        verbose_name='y (m)',
    )
    latitude = models.FloatField(
        verbose_name='latitude (deg)',
    )
    longitude = models.FloatField(
        verbose_name='longitude (deg)',
    )
    speed = models.FloatField(
        verbose_name='speed (km/h)',
    )
