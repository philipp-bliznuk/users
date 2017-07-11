# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import UserAccount, Activity


class ActivityInline(admin.StackedInline):
    model = Activity
    extra = 0


class UserAccountAdmin(admin.ModelAdmin):
    inlines = [ActivityInline]


admin.site.register(UserAccount, UserAccountAdmin)
