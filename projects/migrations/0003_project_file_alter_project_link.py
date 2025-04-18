# Generated by Django 5.1.1 on 2024-10-26 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_project_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='file',
            field=models.FileField(blank=True, help_text='Upload a file related to the project.', null=True, upload_to='files/', verbose_name='Project File'),
        ),
        migrations.AlterField(
            model_name='project',
            name='link',
            field=models.URLField(blank=True, help_text='Enter a link to the project or repository.', null=True),
        ),
    ]
