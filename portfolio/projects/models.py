from django.db import models
from django.utils.text import slugify

class TechnologyType(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Technology Type")

    def __str__(self):
        return self.name

class Technology(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Technology Name")
    type = models.ForeignKey(
        TechnologyType,
        on_delete=models.CASCADE,
        related_name="technologies",
        verbose_name="Type"
    )

    def __str__(self):
        return f"{self.name} ({self.type.name})"

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Project Title")
    slug = models.SlugField(max_length=250, unique=True, blank=True, verbose_name="URL Slug")
    link = models.URLField(help_text="Enter a link to the project or repository.")
    description = models.TextField(verbose_name="Project Description")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Date Created")
    updated = models.DateTimeField(auto_now=True, verbose_name="Last Updated")
    image = models.ImageField(
        upload_to='images/',
        blank=True,
        null=True,
        help_text="Upload an image for the project.",
        verbose_name="Project Image"
    )
    technologies = models.ManyToManyField(Technology, related_name="projects", verbose_name="Technologies Used")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def technology_list(self):
        """Returns a comma-separated list of technologies used in this project."""
        return ", ".join(tech.name for tech in self.technologies.all())

    class Meta:
        ordering = ["-created"]
        verbose_name = "Project"
        verbose_name_plural = "Projects"
