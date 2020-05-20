from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from bug_tracker.models import Tracker, Ticket
# Register your models here.
admin.site.register(Tracker, UserAdmin)
admin.site.register(Ticket)