# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse, reverse
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User, Group

# Create your models here.


class Tposition(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    # create updated_at field as a updated on change Date type field
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
    # create updated_at field as a updated on change Date type field
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
    # create updated_at field as a updated on change Date type field
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
    # create updated_at field as a updated on change Date type field
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
    # create updated_at field as a updated on change Date type field
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        string_output = "id:{} points_earned:{} rank:{} description:{}"
        return string_output.format(
            self.id,
            self.points_earned,
            self.rank,
            self.description
        )
