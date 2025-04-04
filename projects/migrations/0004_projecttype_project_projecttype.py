# Generated by Django 5.1.1 on 2024-11-04 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_project_file_alter_project_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Project Type')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='projecttype',
            field=models.ManyToManyField(related_name='projects', to='projects.projecttype', verbose_name='Project Types'),
        ),
    ]
