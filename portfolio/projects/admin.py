from django.contrib import admin
from .models import TechnologyType, Technology, Project

@admin.register(TechnologyType)
class TechnologyTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ("name", "type")
    list_filter = ("type",)
    search_fields = ("name", "type__name")

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "created", "updated", "technology_list")
    list_filter = ("created", "updated", "technologies__type")
    search_fields = ("title", "description", "technologies__name")
    prepopulated_fields = {"slug": ("title",)}
    ordering = ("-created",)
    readonly_fields = ("created", "updated")
    
    def technology_list(self, obj):
        return obj.technology_list()
    technology_list.short_description = "Technologies Used"