# Generated by Django 4.0.4 on 2022-05-19 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_attendee_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendee',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='phone',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
