from django.contrib import admin

from .models import Mentor, Opinion

admin.site.register([Mentor, Opinion])
