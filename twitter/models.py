from django.db import models
from django.contrib.auth.models import User

class Twit(models.Model):
    text = models.TextField(max_length = 255)
    twit_from = models.CharField(max_length = 255)
    twit_User = models.ForeignKey(User)

    def __unicode__(self):
        return self.text
