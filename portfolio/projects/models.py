from django.db import models


class TechnologyType(models.Model):
    name = models.CharField(max_length=50)  # e.g., "Programming Language", "Cloud Technology"

    def __str__(self):
        return self.name
    
class Technology(models.Model):
    name = models.CharField(max_length=100)  # e.g., "Python", "Azure"
    type = models.ForeignKey(TechnologyType, on_delete=models.CASCADE, related_name="technologies")

    def __str__(self):
        return f"{self.name} ({self.type.name})"

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    technologies = models.ManyToManyField(Technology, related_name="projects")

    def __str__(self):
        return self.title
