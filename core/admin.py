from django.contrib import admin
from .models import contactMessage
from .models import HomePageContent

admin.site.register(contactMessage)
@admin.register(HomePageContent)
class HomePageContent(admin.ModelAdmin):
    list_display = ('title', 'note', 'position')
    list_editable = ('position',)