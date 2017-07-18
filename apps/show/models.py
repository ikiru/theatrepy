# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class DanceType(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        string_output = "id:{} name:{}"
        return string_output.format(
            self.id,
            self.name,
        )


class SpecialSkill(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        string_output = "id:{} name:{}"
        return string_output.format(
            self.id,
            self.name,
        )


class VocalType(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        string_output = "id:{} name:{}"
        return string_output.format(
            self.id,
            self.name,
        )


class Showlist(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        string_output = "id:{} user:{} name:{}"
        return string_output.format(
            self.id,
            self.user,
            self.name,
        )


class Techrolelist(models.Model):
    name = models.CharField(max_length=100):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        string_output = "id:{} name:{}"
        return string_output.format(
            self.id,
            self.name,
        )


class Rolelist(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        string_output = "id:{} name:{} age:{} gender:{} description:{}"
        return string_output.format(
            self.id,
            self.name,
            self.age,
            self.gender,
            self.description,
        )


class ConflictReason(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        string_output = "id:{} name:{}"
        return string_output.format(
            self.id,
            self.name,
        )


class Audtion(models.Model):
    user = models.ForeignKey(User)
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
    techrolelist = models.ForeignKey(techrolelist)
    understudy = models.CharField(max_length=10)
    read_music = models.CharField(max_length=10)
    dancetype = models.ForeignKey(DanceType)
    danceexp = models.TextField()
    vocaltype = models.ForeignKey(VocalType)
    vocalexp = models.TextField()
    specialskill = models.ForeignKey(SpecialSkill)
    note = models.TextField()
    physical_limitation = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
    string_output = "id:{} name:{}age:{}height:{} weight:{} eye:{} hair:{} sex:{}character_one:{} character_two:{} character_three:{}other_role:{} ensemble_role:{} understudy:{} read_music:{}dancetype:{}danceexp:{}vocaltype:{} vocalexp:{}note:{} physical_limitation:{}"
        return string_output.format(
            self.id,
            self.name,
            self.age,
            self.height,
            self.weight,
            self.eye,
            self.hair,
            self.sex,
            self.character_one,
            self.character_two,
            self.character_three,
            self.other_role,
            self.ensemble_role,
            self.understudy,
            self.read_music,
            self.dancetype,
            self.danceexp,
            self.vocaltype,
            self.vocalexp,
            self.note,
            self.physical_limitation,
        )


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        string_output = "id:{} name:{}"
        return string_output.format(
            self.id,
            self.name,
        )


class Venue(models.Model)
    user = models.ForeignKey(User)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.ForeignKey(State)
    zip = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    website = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    school = models.ForeignKey(School)
    in_district = models.BooleanField(default=True)
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        string_output = "id:{} user: {} name:{} address:{} city:{} state:{} zip:{} phone:{} website:{} in_district: {} notes:{}"
        return string_output.format(
            self.id,
            self.user,
            self.name,
            self, address,
            self.city,
            self.state,
            self.zip,
            self.phone,
            self.website,
            self.in_district,
        )


class Conflict(models.Model):
    user = models.ForeignKey(User)
    date = models.DateTimeField(auto_now=True)
    note = models.TextField()
    conflicteason = models.ForeignKey(ConflictReason)
    is_approved = models.BooleanField(defult=false)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        string_output = "id:{} user:{}date:{}note:{} conflicteason:{} is_approved:{}"
        return string_output.format(
            self.id,
            self.user,
            self.date,
            self.note,
            self.conflicteason,
            self.is_approved,
        )
