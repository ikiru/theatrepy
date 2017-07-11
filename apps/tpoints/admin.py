# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

Register your models here.
from . models import Tcatagory, Tposition, Thonor, Tlength, Trank


class TcategoryModel(admin.ModelAdmin):
    list_display = ["name", "updated_at", "created_at"]
    list_display_links = ["name"]
    list_filter = ["name"]
    ist_editable = ["name"]
    search_fields = ["name"]

    class Meta:
        model = Tcategory

    admin.site.register(Tcatagory, TcategoryModel)


class TpositionModel(admin.ModelAdmin):
    list_display = ["name", "updated_at", "created_at"]
    list_display_links = ["name"]
    list_filter = ["name"]
    ist_editable = ["name"]
    search_fields = ["name"]

    class Meta:
        model = TpositionModel


admin.site.register(Tposiiton, TpositionModel)


class ThonorModel(admin.ModelAdmin):
    list_display = ["name", "updated_at", "created_at"]
    list_display_links = ["name"]
    list_filter = ["name"]
    ist_editable = ["name"]
    search_fields = ["name"]

    class Meta:
        model = ThonorModel


admin.site.register(Thonor, ThonorModel)


class TlengthModel(admin.ModelAdmin):
    list_display = ["name", "updated_at", "created_at"]
    list_display_links = ["name"]
    list_filter = ["name"]
    ist_editable = ["name"]
    search_fields = ["name"]

    class Meta:
        model = TlengthModel


admin.site.register(Tlength, TlengthModel)


class TrankModel(admin.ModelAdmin):
    list_display = ["name", "updated_at", "created_at"]
    list_display_links = ["name"]
    list_filter = ["name"]
    ist_editable = ["name"]
    search_fields = ["name"]

    class Meta:
        model = TrankModel


admin.site.register(Trank, TrankModel)
