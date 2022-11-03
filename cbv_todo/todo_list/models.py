from django.db import models


class Task(models.Model):
    TITLE_LEN = 30
    DESC_LEN = 100

    title = models.CharField(max_length=TITLE_LEN)

    description = models.CharField(max_length=DESC_LEN)

    date_created = models.DateTimeField(auto_now_add=True)
