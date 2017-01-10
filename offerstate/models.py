# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Company(models.Model):
    id = models.IntegerField(primary_key=True)
    company_name = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company'


class Offer(models.Model):
    id = models.IntegerField(primary_key=True)
    company_id = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'offer'


class OfferExp(models.Model):
    id = models.IntegerField(primary_key=True)
    offer_id = models.IntegerField(blank=True, null=True)
    offer_experience = models.CharField(max_length=10, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'offer_exp'


class OfferInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    company_id = models.IntegerField(blank=True, null=True)
    offer_subject = models.CharField(max_length=200, blank=True, null=True)
    offer_regist_date = models.CharField(max_length=10, blank=True, null=True)
    offer_state = models.CharField(max_length=10, blank=True, null=True)
    offer_expire_date = models.CharField(max_length=10, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    offer_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'offer_info'


class OfferPosition(models.Model):
    id = models.IntegerField(primary_key=True)
    offer_id = models.IntegerField(blank=True, null=True)
    position = models.CharField(max_length=45, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'offer_position'


class OfferSkills(models.Model):
    id = models.IntegerField(primary_key=True)
    offer_id = models.IntegerField(blank=True, null=True)
    skill_name = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'offer_skills'


class RocketPunch(models.Model):
    id = models.IntegerField(primary_key=True)
    skill_name = models.CharField(max_length=255, blank=True, null=True)
    skill_count = models.IntegerField(blank=True, null=True)
    offer_group = models.IntegerField(blank=True, null=True)
    regist_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rocket_punch'
