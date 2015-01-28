from django.db import models
from django.contrib.auth.models import User
import datetime

class Twit(models.Model):
    text = models.TextField(max_length = 255)
    twit_from = models.CharField(max_length = 255)
    twit_User = models.ForeignKey(User)
    twit_date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.text
