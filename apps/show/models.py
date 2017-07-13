# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Audtion(models.Model):
    age = models.IntField()
    height = models.CharField(max_length=10)
    weight = models.IntField()
    eye = models.CharField(max_length=10)
    hair = models.CharField(max_length=10)
    sex = models.CharField(max_length=10)
    character_one = models.CharField(max_length=10)
    character_two = models.CharField(max_length=10)
    character_three = models.CharField(max_length=10)
    other_role = models.CharField(max_length=10)
    ensemble_role = models.BooleanField(default=True)
    understudy = models.CharField(max_length=10)
    read_music = models.CharField(max_length=10)
    not_cast = models.CharField(max_length=10)
    notes = models.CharField(max_length=10)
    danceexp = models.TextField()
    vocalexp = models.TextField()
    physical_limitation = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Showlist(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Techrolelist(models.Model):
    name = models.CharField(max_length=100):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Rolelist(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Venue(models.Model)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state_id
    zip = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    website = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    school_id
    in_district = models.BooleanField(default=True)
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class DanceType(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ConflictReason(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Conflict(models.Model):
    date = models.DateTimeField(auto_now=True)
    note = models.TextField()
    conflicteason = models.ForeignKey(ConflictReason)
    is_approved = models.BooleanField(defult=false)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
