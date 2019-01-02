from django.db import models

# Create your models here.

class Stoken(models.Model):
    tid = models.CharField(max_length=2)
    device_name = models.CharField(max_length=20, default=tid)
    apiid = models.CharField(max_length=18, default='bl397233b7de02c055')
    apikey = models.CharField(max_length=32, default='da5cbd210dbd9e994a9fdf5731aaae51')
    expires_in = models.CharField(max_length=100)
    access_token = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'keyM'
        verbose_name_plural = verbose_name
