# Generated by Django 5.1.1 on 2024-10-13 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmessage',
            name='reason',
            field=models.CharField(choices=[('general', 'General Enquiry'), ('feedback', 'Feedback'), ('permanent', 'Hire Me!'), ('tutoring', 'Tutoring')], max_length=100),
        ),
    ]
