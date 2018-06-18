# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desidered behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Follower(models.Model):
    fol_code = models.AutoField(primary_key=True)
    fol_mail = models.CharField(max_length=100, blank=True, null=True)
    fol_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'follower'


class Followers(models.Model):
    fol_code = models.AutoField(primary_key=True)
    fol_mail = models.CharField(max_length=100, blank=True, null=True)
    fol_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'followers'


class Personas(models.Model):
    dni = models.CharField(primary_key=True, max_length=20)
    username = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    names = models.CharField(max_length=50, blank=True, null=True)
    lastname = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    web = models.CharField(max_length=100, blank=True, null=True)
    borndate = models.DateField(blank=True, null=True)
    lastconnection = models.DateField(blank=True, null=True)
    photo = models.CharField(max_length=200, blank=True, null=True)
    information = models.CharField(max_length=20, blank=True, null=True)
    usertype = models.CharField(max_length=1, blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personas'
