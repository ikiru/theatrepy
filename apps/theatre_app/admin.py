# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from . models import District, School, State, Gradyear, Profile


class DistrictModel(admin.ModelAdmin):
    list_display = ["name", "updated_at", "created_at"]
    list_display_links = ["name"]
    list_filter = ["name"]
    list_editable = ["name"]
    search_fields = ["name"]

    class Meta:
        model = District


admin.site.register(District, DistrictModel)


class SchoolModel(admin.ModelAdmin):
    list_display = ["name",  "district", "address",
                    "zip", "phone", "updated_at", "created_at"]
    list_editable = ["name", "district", "address", "zip", "phone"]
    list_filter = ["name"]
    search_fields = ["name"]

    class Meta:
        model = School


admin.site.register(School)


class StateModel(admin.ModelAdmin):
    list_display = ["name", "updated_at", "created_at"]
    list_editable = ["name"]
    list_filter = ["name"]
    search_fields = ["name"]

    class Meta:
        model = State


admin.site.register(State)


class GradYearModel(admin.ModelAdmin):
    list_display = ["name", "updated_at", "created_at"]
    list_editable = ["name"]
    list_filter = ["name"]
    search_fields = ["name"]

    class Meta:
        model = Gradyear


admin.site.register(Gradyear)


class ProfileModel(admin.ModelAdmin):
    list_display = ["name", "updated_at", "created_at"]
    list_editable = ["name"]
    list_filter = ["name"]
    search_fields = ["name"]

    class Meta:
        model = Profile


admin.site.register(Profile)
