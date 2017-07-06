# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse, reverse
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User, Group

# Create your models here.


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


class District(models.Model):
    name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    # create updated_at field as a updated on change Date type field
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        string_output = "id:{} name:{}"
        return string_output.format(
            self.id,
            self.name,
        )


class School(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District)
    created_at = models.DateTimeField(auto_now_add=True)
    # create updated_at field as a updated on change Date type field
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        string_output = "id:{} name:{}district{}"
        return string_output.format(
            self.id,
            self.name,
            self.district,
        )


class State(models.Model):
    name = models.CharField(max_length=45)
    district = models.ForeignKey(District)
    school = models.ForeignKey(School)
    created_at = models.DateTimeField(auto_now_add=True)
    # create updated_at field as a updated on change Date type field
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        string_output = "id:{} name:{}district{}"
        return string_output.format(
            self.id,
            self.name,
            self.district,
            self.school,
        )


class Gradyear(models.Model):
    year = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    # create updated_at field as a updated on change Date type field
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        string_output = "id:{} year:{}profile"
        return string_output.format(
            self.id,
            self.year,
            self.profile,
        )


class Profile(models.Model):
    user = models.OneToOneField(User)
    group = models.ForeignKey(Group)
    address = models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    state = models.CharField(max_length=45)
    zip = models.CharField(max_length=45)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=45)
    mobile = models.CharField(max_length=45)
    district = models.ForeignKey(District)
    school = models.ForeignKey(School)
    gradyear = models.ForeignKey(Gradyear)
    avatar = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        string_output = "id:{} address:{} city:{} state{} zip{} email{} phone{} district{} school{} image{}"
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
            self.avatar,
        )
