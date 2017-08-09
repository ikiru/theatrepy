# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse, reverse
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User, Group

#
#
#
#
# Base user models
#
#
#
#


class Profilemanager(models.Manager):
    def validate(self, form_data):
        errors = []  # arrary where we will store the error messages

        if len(form_data['address']) == 0 and len(form_data['address']) > 3:
            # check if address is blank
            errors.append(
                "Address is required and must be at least 3 characters")

        if len(form_data['zip']) == 0 and len(form_data['zip']) > 5:
            # check if zip is blank
            errors.append(
                "Zip code is required and must be at least 5 characters.")

        if len(form_data['email']) == 0:
            errors.append("email required.")  # check if email is blank

        if len(form_data['mobile']) == 0 and len(form_data['mobile']) > 3:
            # check if mobile is blank
            errors.append(
                "Mobie Phone number is required to recieve mobil alerts.")

        return errors  # send error messages to the  page


class School(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100, null=True)
    zip = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=20,  null=True)
    logo = models.CharField(max_length=200,  null=True)
    prim_color = models.CharField(max_length=20,  null=True)
    sec_color = models.CharField(max_length=20,  null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        string_output = "id:{} name:{}address:{}zip:{} phone:{} logo:{} prim_color:{} sec_color:{}"
        return string_output.format(
            self.id,
            self.name,
            self.address,
            self.zip,
            self.phone,
            self.logo,
            self.prim_color,
            self.sec_color,
        )


class District(models.Model):
    name = models.CharField(max_length=45)
    school = models.ForeignKey(School)
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


class State(models.Model):
    name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        string_output = "id:{} name:{}district{}"
        return string_output.format(
            self.id,
            self.name,
        )


class Gradyear(models.Model):
    year = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.year

    def __str__(self):
        string_output = "id:{} year:{}"
        return string_output.format(
            self.id,
            self.year,
        )


class Profile(models.Model):
    user = models.OneToOneField(User)
    group = models.ForeignKey(Group)
    address = models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    state = models.ForeignKey(State)
    district = models.ForeignKey(District)
    school = models.ForeignKey(School)
    zip = models.CharField(max_length=45)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=45)
    mobile = models.CharField(max_length=45)
    district = models.ForeignKey(District)
    school = models.ForeignKey(School)
    gradyear = models.ForeignKey(Gradyear)
    is_active = models.BooleanField(default=True)
    avatar = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.user

    def __str__(self):
        string_output = "id:{} address:{} city:{} state{} zip{} email{} phone{} district{} school{}gradyear{} is_active{} image{}"
        return string_output.format(
            self.id,
            self.address,
            self.city,
            self.state,
            self.zip,
            self.email,
            self.phone,
            self.mobile,
            self.district,
            self.school,
            self.gradyear,
            self.avatar,
        )

#
#
#
#
# thespian Points
#
#
#
#


class Tposition(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        string_output = "id:{} name:{}"
        return string_output.format(
            self.id,
            self.name,
        )


class Trank(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        string_output = "id:{} name:{}"
        return string_output.format(
            self.id,
            self.name,
        )


class Tlength(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        string_output = "id:{} name:{}"
        return string_output.format(
            self.id,
            self.name,
        )


class Tcategory(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        string_output = "id:{} name:{}"
        return string_output.format(
            self.id,
            self.name,
        )


class Thonor(models.Model):
    points_earned = models.IntegerField()
    rank = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        string_output = "id:{} points_earned:{} rank:{} description:{}"
        return string_output.format(
            self.id,
            self.points_earned,
            self.rank,
            self.description
        )

#
#
#
#
# Show models
#
#
#
#


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
    user = models.ForeignKey(User)
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
    age = models.IntegerField()
    height = models.CharField(max_length=10)
    weight = models.IntegerField()
    eye = models.CharField(max_length=10)
    hair = models.CharField(max_length=10)
    sex = models.CharField(max_length=10)
    character_one = models.CharField(max_length=10)
    character_two = models.CharField(max_length=10)
    character_three = models.CharField(max_length=10)
    other_role = models.CharField(max_length=10)
    ensemble_role = models.BooleanField(default=True)
    techrolelist = models.ForeignKey(Techrolelist)
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


class Directorsnote(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User)
    school = models.ForeignKey(School)
    showlist = models.ForeignKey(Showlist)
    audition = models.ForeignKey(Audtion)
    reading = models.IntegerField()
    characterization = models.IntegerField()
    direction = models.IntegerField()
    vocal = models.IntegerField()
    movement = models.IntegerField()
    reading_note = models.TextField()
    characterization_note = models.TextField()
    direction_note = models.TextField()
    vocal_note = models.TextField()
    movement_note = models.TextField()
    overall_note = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        string_output = "id:{} name:{} school:{} show:{} audition:{}reading:{} characterization:{} direction:{} vocal:{} movement:{} characterization_note:{} direction_note:{} vocal_note:{} movement_note:{} reading_note:{} overall_note:{}"
        return string_output.format(
            self.id,
            self.user,
            self.school,
            self.show,
            self.audition,
            self.reading,
            self.characterization,
            self.direction,
            self.vocal,
            self.movement,
            self.characterization_note,
            self.direction_note,
            self.vocal_note,
            self.movement_note,
            self.reading_note,
            self.overall_note,
            self.updated_at,
            self.created_at,
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


class Venue(models.Model):
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
    is_approved = models.BooleanField()
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


#
#
#
#
# Dontions  and fundraiser Models
#
#
#
#

    class Donor(models.Model):
        user = models.ForeignKey(User)
        firstname = models.CharField(max_length=100)
        lastname = models.CharField(max_length=100)
        business_name = models.CharField(max_length=100)
        address = models.CharField(max_length=100)
        city = models.CharField(max_length=100)
        state = models.ForeignKey(State)
        zip = models.CharField(max_length=100)
        phone = models.CharField(max_length=100)
        is_active = models.BooleanField()
        note = models.TextField()
        email = models.CharField(max_length=100)
        school_id = models.CharField(max_length=100)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        def __unicode__(self):
            return self.name

        def __str__(self):
            string_output = "id:{} user:{}firstname:{}lastname:{}business_name:{}address:{} city:{} state_id:{} zip:{} phone:{} is_active:{} date:{}note:{} note:{} email:{} school_id:{} "
            return string_output.format(
                self.id,
                self.user,
                self.firstname,
                self.lastname,
                self.business_name,
                self.address,
                self.city,
                self.state_id,
                self.zip,
                self.phone,
                self.is_active,
                self.date,
                self.note,
                self.email,
                self.school_id,
            )

    class Donortype(models.Model):
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

    class Donationtype(models.Model):
        name = models.CharField(max_length=100)
        user = models.CharField(max_length=100)
        name = models.CharField(max_length=100)
        donor = models.ForeignKey(Donor)
        date = models.DateField()
        donationtype = models.ForeignKey(Donationtype)
        note = models.TextField()
        has_receipt = models.BooleanField()
        school = models.ForeignKey(School)
        value = models.IntegerField()
        upload = models.CharField(max_length=200)
        updated_at = models.DateTimeField(auto_now=True)
        created_at = models.DateTimeField(auto_now_add=True)

        def __unicode__(self):
            return self.name

        def __str__(self):
            string_output = "id:{} name:{}"
            return string_output.format(
                self.id,
                self.user,
                self.name,
                self.donor,
                self.date,
                self.donationtype,
                self.note,
                self.has_receipt,
                self.school,
                self.value,
                self.upload,
                self.updated_at,
                self.created_at,
            )

#
#
#
#
# Budget Models
#
#
#
#

    class Budgetcatagory(models.Model):
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

    class Budgetexpense(models.Model):
        name = models.CharField(max_length=100)
        user = models.ForeignKey(User)
        school = models.ForeignKey(School)
        # budgetcatagory = models.ForeignKey(Budgetcatagory)
        amount = models.IntegerField()
        has_receipt = models.BooleanField()
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        def __unicode__(self):
            return self.name

        def __str__(self):
            string_output = "id:{} name:{} user:{} school:{} budgetitem:{} amount: {} has_receipt:{}"
            return string_output.format(
                self.id,
                self.name,
                self.user,
                self.school,
                self.budgetitem,
                self, amount,
                self.has_receipt,
            )
