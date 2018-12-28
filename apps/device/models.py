from django.db import models

# Create your models here.

class Stoken(models.Model):
    expires_in = models.DateTimeField(auto_now_add=True)
    access_token = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'keyM'
        verbose_name_plural = verbose_name
