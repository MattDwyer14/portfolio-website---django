from django.contrib import admin
from .models import contactMessage
from .models import HomePageContent

admin.site.register(HomePageContent)
admin.site.register(contactMessage)
