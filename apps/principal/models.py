from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Follower(models.Model):
    fol_code = models.AutoField(primary_key=True)
    fol_mail = models.CharField(max_length=100, blank=True, null=True)
    fol_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'follower'
