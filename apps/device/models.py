from django.db import models

# Create your models here.

class Stoken(models.Model):
    tid = models.CharField(max_length=2)
    expires_in = models.CharField(max_length=100)
    access_token = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'keyM'
        verbose_name_plural = verbose_name
